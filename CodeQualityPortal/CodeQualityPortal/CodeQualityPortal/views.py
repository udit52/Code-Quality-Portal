"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, request, url_for, Response
from CodeQualityPortal.forms import SubmitRepositoryForm, ChooseMetricsForm
from CodeQualityPortal import app
from CodeQualityPortal import sql_db
import logging
import requests
import os
import base64
import re
import math
import json
import lizard
import subprocess
import pandas as pd

logger = logging.getLogger(__name__)

url_root = "https://api.github.com"

token = "8fede56e8b1ee9ac65d84b4b2b9ccec65c19d7db"

headers = {
    "content-type": "application/json",
    "Authorization": "token " + token,
    "Accept": "application/vnd.github.squirrel-girl-preview+json",
}



class ClassContent(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.first_line = 0
        self.last_line = 0
        self.parents = []
        self.no_of_methods = 0
        self.no_of_comments = 0
        self.cyclomatic_complexity = 0


def strip_generalize_class(class_name):
    if "<" in class_name:
        class_name = class_name[:class_name.index("<")]
    return class_name.replace("{","").strip()


def parse_file_content(content, file_name, class_objects):
    function_regex = "(public|protected|private|static|abstract|synchronized|final|transient|volatile|native|strictfp|\s)*[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *(\{?|[^;])"
    lines = content.split("\n")

    class_size_pointer = {}
    other = 0
    class_stack = []
    multi_comment_flag = False
    for i, line in enumerate(lines):
        # print(i,line)
        if "*/" in line:
            if class_stack:
                class_objects[class_stack[-1]].no_of_comments += 1

            multi_comment_flag = False

        if multi_comment_flag:
            if class_stack:
                class_objects[class_stack[-1]].no_of_comments += 1
            continue

        prev = line
        line = line.split("//")[0]
        if prev != line:
            if class_stack:
                class_objects[class_stack[-1]].no_of_comments += 1
        words = line.split(" ")

        if "/*" in line:
            if "*/" in line:
                continue
            multi_comment_flag = True
            continue

        if "class" in words or "interface" in words:

            # create class object
            class_content = ClassContent(file_name)

            # save line where class is found
            class_content.first_line = i

            # get class name and store objects
            if "interface" in words:
                class_name = strip_generalize_class(words[words.index("interface") + 1])
            else:
                class_name = strip_generalize_class(words[words.index("class") + 1])

            # Add parent of the current class if it exists (for nested classes)
            if class_stack:
                class_content.parents.append(class_stack[-1])

            if "extends" in words:
                class_content.parents.append(strip_generalize_class(words[words.index("extends") + 1]))

            if "implements" in words:
                t = line[line.index("implements") + 11:]
                p = t.split(",")

                for x in p[:len(p) - 1]:
                    class_content.parents.append(strip_generalize_class(x))

                if "{" in p[len(p) - 1]:
                    last = p[len(p) - 1].strip()[:-1]
                else:
                    last = p[len(p) - 1]
                class_content.parents.append(strip_generalize_class(last))

            # Lines of code
            if "{" in line:
                class_size_pointer[class_name] = 1
            else:
                class_size_pointer[class_name] = -1
            class_stack.append(class_name)
            class_objects[class_name] = class_content
        elif "{" in line:
            open_braces = line.count("{")
            if not class_stack:
                other += open_braces
                continue
            recent_class = class_stack[-1]
            if class_size_pointer[recent_class] == -1:
                class_size_pointer[recent_class] = 1
                open_braces -= 1
                other += open_braces
            else:
                other += open_braces
        if "}" in line:
            close_braces = line.count("}")
            if other == 0:
                recent_class = class_stack.pop()
                class_size_pointer[recent_class] = 0
                class_objects[recent_class].last_line = i
            else:
                other -= close_braces
                if other < 0:
                    count_class = math.abs(other)
                    for i in range(count_class):
                        recent_class = class_stack.pop()
                        class_size_pointer[recent_class] = 0
                        class_objects[recent_class].last_line = i
                    other = 0

        # Number of methods per class
        if "=" not in line and re.match(function_regex, line):
            if class_objects[class_stack[-1]].no_of_methods is None:
                class_objects[class_stack[-1]].no_of_methods = 0
            class_objects[class_stack[-1]].no_of_methods += 1

@app.route('/', methods=['GET', 'POST'])
def index():
    """Renders the home page."""

    form = SubmitRepositoryForm()
    print(request.args.getlist('error'))

    if request.method == "POST":
        if form.validate_on_submit():
            repo_name = ""
            owner = ""
            try:
                repo_url = request.form["repo_url"]
                data = repo_url.split("/")
                owner = data[3]
                repo_name = data[4]
            except:
                form.repo_url.errors.append("Invalid Github Repository URL")

            return render_template(
                'index.html',
                form=form,
                repo_name=repo_name,
                owner=owner,
                flag="1"
            )

    return render_template(
        'index.html',
        form=form,
        repo_name="",
        owner="",
        flag="0"
    )

@app.route('/progress/<repo_name>/<owner>')
def progress(repo_name, owner):

    def generate():
        repo_root_url = os.path.join(url_root, "repos", owner, repo_name, "branches/master")
        response = requests.get(repo_root_url, headers=headers)
        print(response)
        if response.status_code != 200:
            yield "data:" + "99" + "\n\n"
        else:
            response = response.json()
            tree_sha = response["commit"]["sha"]
            repo_tree_url = os.path.join(url_root, "repos", owner, repo_name, "git/trees", tree_sha + "?recursive=1")

            response = requests.get(repo_tree_url, headers=headers)
            response = response.json()

            tree = response["tree"]

            class_objects = {}
            count = 0
            for x in tree:
                if ".java" in x["path"]:
                    response = requests.get(x["url"], headers=headers)
                    if "content" in response.json():
                        response = response.json()["content"]
                        content = base64.b64decode(response)
                        file_name = x["path"].split("/")[-1]
                        print(file_name)

                        yield "data:" + x["path"] + "\n\n"

                        parse_file_content(str(content, "utf-8"), file_name, class_objects)
                        print(file_name)
                        with(open(file_name, "w")) as f:
                            f.write(str(content, "utf-8"))
                            f.close()
                        cmd = ["lizard", "--csv", file_name]
                        with open('out.csv', 'w') as fout:
                            subprocess.call(cmd, stdout=fout, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                            fout.close()

                        df = pd.read_csv("out.csv", header=None,
                                         names=['nloc', 'ccn', 'token', 'param', 'length', 'location', 'filename', 'methodname',
                                                'methodparams', 'a', 'b'])

                        df["class_name"] = df["location"].map(lambda x: x.split("@")[0])
                        for i in range(len(df)):
                            try:
                                df.at[i, "class_name"] = strip_generalize_class(df.at[i, "class_name"].split("::")[-2])
                            except:
                                df.at[i, "class_name"] = None
                        class_ccn = df.groupby("class_name")["ccn"].max()
                        for key, val in class_ccn.iteritems():
                            if key:
                                class_objects[key].cyclomatic_complexity = val
                        os.remove(file_name)
            yield "data:" + "100" + "\n\n"
            header = {
                "content-type": "application/json",
                "Authorization": "token " + token,
                'Accept': 'application/vnd.github.hellcat-preview+json'
            }
            response_collab = requests.get(url_root + '/repos/' + owner + '/' + repo_name + '/stats/contributors',
                                           headers=header)
            response_collab = response_collab.json()
            r = response_collab[-1]
            major_collab = r["author"]["login"]
            print(major_collab)

            total_collab = 0
            for i in range(1, 10):
                response = requests.get(
                    url_root + '/repos/' + owner + '/' + repo_name + '/contributors?page=' + str(i) + '&per_page=1000',
                    headers=header)
                response = response.json()
                total_collab += len(response)
            print(total_collab)

            sql_db.mock_database_generator(class_objects, repo_name, major_collab, total_collab)
    return Response(generate(), mimetype='text/event-stream')

@app.route('/choose-metric', methods=['GET', 'POST'])
def choose_metric():
    """Renders the contact page."""
    form = ChooseMetricsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            metrics = []
            print(request.form)
            if 'comments_or_documentation' in request.form:
                metrics.append('Comments or Documentation')
            if 'no_of_methods_per_class' in request.form:
                metrics.append('No. of Methods per Class')
            if 'cyclomatic_complexity' in request.form:
                metrics.append('Cyclomatic Complexity')
            if 'no_of_collaborators_per_file' in request.form:
                metrics.append('No. of Collaborators per File')
            if 'lines_of_code' in request.form:
                metrics.append('Lines of Code')
            if 'class_hierarchy_level' in request.form:
                metrics.append('Class Hierarchy Level')

            return redirect(url_for('visualisations', metrics=metrics))

    return render_template(
        'choose-metric.html',
        form=form
    )

@app.route('/visualisations', methods=['GET', 'POST'])
def visualisations():
    """Renders the about page."""
    metrics = request.args.getlist('metrics')
    print(metrics)
    return render_template(
        'visualisations.html',
        metrics=metrics
    )




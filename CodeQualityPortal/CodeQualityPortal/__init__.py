"""
The flask application package.
"""

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-key-here'

import CodeQualityPortal.views
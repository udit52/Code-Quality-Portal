import mysql.connector
import datetime


def mock_database_generator():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="password",
	  database="Github_Mining"
	)

	x=str(datetime.datetime.now() - datetime.timedelta(days=3*365))
	y=str(datetime.datetime.now() - datetime.timedelta(days=2.5*365))
	z=str(datetime.datetime.now() - datetime.timedelta(days=2*365))
	a=str(datetime.datetime.now() - datetime.timedelta(days=1.5*365))
	b=str(datetime.datetime.now() - datetime.timedelta(days=1*365))
	mycursor = mydb.cursor()

	# mycursor.execute("CREATE DATABASE Github_Mining")
	mycursor.execute("CREATE TABLE IF NOT EXISTS File_Records (ID INT AUTO_INCREMENT PRIMARY KEY, TimeStamp  DATETIME,Repo_Name VARCHAR(255),File_Name Varchar(255), Total_Methods INT,Class_Name VARCHAR(255),Parent VARCHAR(255), Coupling INT, LOC INT,Total_Collaborator INT,Major_Collaborator Varchar(255))")

	mycursor.execute("CREATE TABLE IF NOT EXISTS Project_Records (ID INT AUTO_INCREMENT PRIMARY KEY, TimeStamp DATETIME, CyclomaticComplexity INT, FraudDetection INT)")

	sql = "INSERT INTO File_Records (TimeStamp,Repo_Name,Total_Methods,File_Name,Class_Name,Parent,Coupling,LOC,Total_Collaborator,Major_Collaborator) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val=[
	(x,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(x,'Bank Account',20,'Accounts',"Current",'Account',0,350,9,"niks"),
	(x,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(x,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(x,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2100,4,'rish'),
	(x,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(y,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(y,'Bank Account',20,'Accounts',"Current",'Account',0,350,9,"niks"),
	(y,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(y,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(y,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2100,4,'rish'),
	(y,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(y,'Bank Account',4,'Accounts',"Joint","Account",5,550,3,"niks"),
	(y,'Bank Account',5,'Accounts',"Fixed","Account",5,650,7,"niks"),
	(y,'Bank Account',2,'Accounts',"Reserved","Account",4,750,4,"niks"),
	(y,'Bank Account',10,'AllEmployees',"Regional","Manager",6,350,2,"niks"),
	(y,'Bank Account',9,'AllEmployees',"Branch","Manager",2,450,5,"niks"),
	(z,'Bank Account',12,'Accounts',"Account",None,5,250,4,"niks"),
	(z,'Bank Account',19,'Accounts',"Current",'Account',0,350,9,"niks"),
	(z,'Bank Account',17,'Accounts',"Saving",'Account',0,500,5,"louis"),
	(z,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(z,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2000,4,'rish'),
	(z,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(z,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(z,'Bank Account',22,'Accounts',"Current",'Account',0,350,9,"niks"),
	(z,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(z,'Bank Account',20,'AllEmployees',"Employees",None,1,700,3,"faz"),
	(z,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2300,4,'rish'),
	(z,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,750,3,'rish'),
	(z,'Bank Account',4,'Accounts',"Joint","Account",5,750,3,"niks"),
	(z,'Bank Account',5,'Accounts',"Fixed","Account",5,550,7,"niks"),
	(z,'Bank Account',2,'Accounts',"Reserved","Account",4,650,4,"niks"),
	(z,'Bank Account',10,'AllEmployees',"Regional","Manager",6,350,2,"niks"),
	(z,'Bank Account',10,'AllEmployees',"Branch","Manager",2,350,5,"niks"),
	(z,'Bank Account',10,'AllCustomers',"Customer",None,2,350,5,"niks"),
	(z,'Bank Account',10,'AllCustomers',"PlatinumMember","Customer",4,450,4,"niks"),
	(z,'Bank Account',10,'AllCustomers',"GoldMember","Customer",2,250,3,"riks"),
	(z,'Bank Account',10,'AllEmployees',"LoanOfficer","Employees",5,650,3,"niks"),
	(z,'Bank Account',10,'AllEmployees',"IT","Employees",4,550,2,"miks"),
	(a,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(a,'Bank Account',20,'Accounts',"Current",'Account',0,350,9,"niks"),
	(a,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(a,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(a,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2100,4,'rish'),
	(a,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(a,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(a,'Bank Account',20,'Accounts',"Current",'Account',0,350,9,"niks"),
	(a,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(a,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(a,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2100,4,'rish'),
	(a,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(a,'Bank Account',4,'Accounts',"Joint","Account",5,550,3,"niks"),
	(a,'Bank Account',5,'Accounts',"Fixed","Account",5,650,7,"niks"),
	(a,'Bank Account',2,'Accounts',"Reserved","Account",4,750,4,"niks"),
	(a,'Bank Account',10,'AllEmployees',"Regional","Manager",6,350,2,"niks"),
	(a,'Bank Account',9,'AllEmployees',"Branch","Manager",2,450,5,"niks"),
	(a,'Bank Account',12,'Accounts',"Account",None,5,250,4,"niks"),
	(a,'Bank Account',19,'Accounts',"Current",'Account',0,450,9,"niks"),
	(a,'Bank Account',17,'Accounts',"Saving",'Account',0,500,5,"louis"),
	(a,'Bank Account',20,'AllEmployees',"Employees",None,1,400,3,"faz"),
	(a,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2000,4,'rish'),
	(a,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(a,'Bank Account',10,'Accounts',"Account",None,5,350,4,"niks"),
	(a,'Bank Account',22,'Accounts',"Current",'Account',0,350,9,"niks"),
	(a,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(a,'Bank Account',20,'AllEmployees',"Employees",None,1,700,3,"faz"),
	(a,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2300,4,'rish'),
	(a,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,750,3,'rish'),
	(a,'Bank Account',4,'Accounts',"Joint","Account",4,750,3,"niks"),
	(a,'Bank Account',5,'Accounts',"Fixed","Account",5,550,7,"niks"),
	(a,'Bank Account',2,'Accounts',"Reserved","Account",4,650,4,"niks"),
	(a,'Bank Account',10,'AllEmployees',"Regional","Manager",6,350,2,"niks"),
	(a,'Bank Account',10,'AllEmployees',"Branch","Manager",2,350,5,"niks"),
	(a,'Bank Account',10,'AllCustomers',"Customer",None,2,350,5,"niks"),
	(a,'Bank Account',10,'AllCustomers',"PlatinumMember","Customer",4,450,4,"niks"),
	(a,'Bank Account',10,'AllCustomers',"GoldMember","Customer",2,250,3,"riks"),
	(a,'Bank Account',10,'AllEmployees',"LoanOfficer","Employees",5,650,3,"niks"),
	(a,'Bank Account',10,'AllEmployees',"IT","Employees",4,550,2,"miks"),
	(a,'Bank Account',11,'AllServices',"Services",None,4,450,3,"alom"),
	(a,'Bank Account',13,'AllServices',"Loan","Services",3,550,2,"malom"),
	(a,'Bank Account',5,'AllServices',"CreditCard","Services",5,250,4,"nalom"),
	(a,'Bank Account',4,'ITEmployees',"IT",None,4,450,3,"alom"),
	(a,'Bank Account',4,'ITEmployees',"Admin","IT",3,1050,7,"nalom"),
	(a,'Bank Account',4,'ITEmployees',"DBA","IT",5,650,4,"niks"),
	(b,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(b,'Bank Account',20,'Accounts',"Current",'Account',0,350,9,"niks"),
	(b,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(b,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(b,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2100,4,'rish'),
	(b,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(b,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(b,'Bank Account',20,'Accounts',"Current",'Account',0,350,9,"niks"),
	(b,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(b,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(b,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2100,4,'rish'),
	(b,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(b,'Bank Account',4,'Accounts',"Joint","Account",5,550,3,"niks"),
	(b,'Bank Account',5,'Accounts',"Fixed","Account",5,650,7,"niks"),
	(b,'Bank Account',2,'Accounts',"Reserved","Account",4,750,4,"niks"),
	(b,'Bank Account',10,'AllEmployees',"Regional","Manager",6,350,2,"niks"),
	(b,'Bank Account',9,'AllEmployees',"Branch","Manager",2,450,5,"niks"),
	(b,'Bank Account',12,'Accounts',"Account",None,5,250,4,"niks"),
	(b,'Bank Account',19,'Accounts',"Current",'Account',0,350,9,"niks"),
	(b,'Bank Account',17,'Accounts',"Saving",'Account',0,500,5,"louis"),
	(b,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(b,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2000,4,'rish'),
	(b,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(b,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(b,'Bank Account',22,'Accounts',"Current",'Account',0,350,9,"niks"),
	(b,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(b,'Bank Account',20,'AllEmployees',"Employees",None,1,700,3,"faz"),
	(b,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2300,4,'rish'),
	(b,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,750,3,'rish'),
	(b,'Bank Account',4,'Accounts',"Joint","Account",5,750,3,"niks"),
	(b,'Bank Account',5,'Accounts',"Fixed","Account",5,550,7,"niks"),
	(b,'Bank Account',2,'Accounts',"Reserved","Account",4,650,4,"niks"),
	(b,'Bank Account',10,'AllEmployees',"Regional","Manager",6,350,2,"niks"),
	(b,'Bank Account',10,'AllEmployees',"Branch","Manager",2,350,5,"niks"),
	(b,'Bank Account',10,'AllCustomers',"Customer",None,2,350,5,"niks"),
	(b,'Bank Account',10,'AllCustomers',"PlatinumMember","Customer",4,450,4,"niks"),
	(b,'Bank Account',10,'AllCustomers',"GoldMember","Customer",2,250,3,"riks"),
	(b,'Bank Account',10,'AllEmployees',"LoanOfficer","Employees",5,650,3,"niks"),
	(b,'Bank Account',10,'AllEmployees',"IT","Employees",4,550,2,"miks"),
	(b,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(b,'Bank Account',20,'Accounts',"Current",'Account',0,350,9,"niks"),
	(b,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(b,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(b,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2100,4,'rish'),
	(b,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(b,'Bank Account',10,'Accounts',"Account",None,5,250,4,"niks"),
	(b,'Bank Account',20,'Accounts',"Current",'Account',0,350,9,"niks"),
	(b,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(b,'Bank Account',20,'AllEmployees',"Employees",None,1,600,3,"faz"),
	(b,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2300,4,'rish'),
	(b,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,500,3,'rish'),
	(b,'Bank Account',4,'Accounts',"Joint","Account",5,550,3,"niks"),
	(b,'Bank Account',5,'Accounts',"Fixed","Account",5,550,7,"niks"),
	(b,'Bank Account',2,'Accounts',"Reserved","Account",4,750,4,"niks"),
	(b,'Bank Account',10,'AllEmployees',"Regional","Manager",6,350,2,"niks"),
	(b,'Bank Account',9,'AllEmployees',"Branch","Manager",2,450,5,"niks"),
	(b,'Bank Account',12,'Accounts',"Account",None,5,250,4,"niks"),
	(b,'Bank Account',19,'Accounts',"Current",'Account',0,350,9,"niks"),
	(b,'Bank Account',17,'Accounts',"Saving",'Account',0,500,5,"louis"),
	(b,'Bank Account',20,'AllEmployees',"Employees",None,1,350,3,"faz"),
	(b,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2000,4,'rish'),
	(b,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,400,3,'rish'),
	(b,'Bank Account',10,'Accounts',"Account",None,5,350,4,"niks"),
	(b,'Bank Account',22,'Accounts',"Current",'Account',0,450,9,"niks"),
	(b,'Bank Account',15,'Accounts',"Saving",'Account',0,400,5,"louis"),
	(b,'Bank Account',20,'AllEmployees',"Employees",None,1,400,3,"faz"),
	(b,'Bank Account',12,'AllEmployees',"Manager",'Employees',6,2300,4,'rish'),
	(b,'Bank Account',13,'AllEmployees',"Teller",'Employees',4,750,3,'rish'),
	(b,'Bank Account',4,'Accounts',"Joint","Account",4,750,3,"niks"),
	(b,'Bank Account',5,'Accounts',"Fixed","Account",5,550,4,"niks"),
	(b,'Bank Account',2,'Accounts',"Reserved","Account",4,650,4,"niks"),
	(b,'Bank Account',10,'AllEmployees',"Regional","Manager",6,350,2,"niks"),
	(b,'Bank Account',10,'AllEmployees',"Branch","Manager",2,350,5,"niks"),
	(b,'Bank Account',10,'AllCustomers',"Customer",None,2,350,5,"niks"),
	(b,'Bank Account',10,'AllCustomers',"PlatinumMember","Customer",4,550,4,"niks"),
	(b,'Bank Account',10,'AllCustomers',"GoldMember","Customer",2,250,3,"riks"),
	(b,'Bank Account',10,'AllEmployees',"LoanOfficer","Employees",5,650,3,"niks"),
	(b,'Bank Account',10,'AllEmployees',"IT","Employees",4,550,2,"miks"),
	(b,'Bank Account',11,'AllServices',"Services",None,4,450,3,"alom"),
	(b,'Bank Account',13,'AllServices',"Loan","Services",3,550,2,"malom"),
	(b,'Bank Account',5,'AllServices',"CreditCard","Services",5,250,4,"nalom"),
	(b,'Bank Account',4,'ITEmployees',"IT",None,4,450,3,"alom"),
	(b,'Bank Account',4,'ITEmployees',"Admin","IT",3,1050,7,"nalom"),
	(b,'Bank Account',4,'ITEmployees',"DBA","IT",5,650,4,"niks"),
	(b,'Bank Account',3,'AllServices',"DebitCard","Saving",6,750,3,"niks"),
	(b,'Bank Account',5,'AllServices',"FixedDeposit","Services",6,850,4,"miks"),
	]
	mycursor.executemany(sql, val)
	mydb.commit()
	#sqlQuery = "WITH RECURSIVE class_path AS ( SELECT Class_Name, Child Child_Class_Name, 1 lvl FROM File_Records WHERE Child IS NULL UNION ALL SELECT f.Class_Name, f.Child, lvl+1 FROM File_Records f INNER JOIN class_path cp ON cp.Class_Name = f.Child )"
	#sqlQuery1="SELECT Class_Name,Child_Class,lvl FROM class_path cp ORDER BY lvl"

	sql1 = 'INSERT INTO Project_Records(TimeStamp,CyclomaticComplexity,FraudDetection) VALUES (%s,%s,%s);'
	val1=[
	(x,14,7),
	(x,14,5),
	(x,12,2),
	(x,13,2),
	(x,11,1),
	(x,11,1),
	(y,14,7),
	(y,14,5),
	(y,12,2),
	(y,13,2),
	(y,11,1),
	(y,11,1),
	(y,15,2),
	(y,9,3),
	(y,7,4),
	(y,5,1),
	(y,6,2),
	(z,14,7),
	(z,14,5),
	(z,12,2),
	(z,13,2),
	(z,11,1),
	(z,11,1),
	(z,14,7),
	(z,14,5),
	(z,12,2),
	(z,12,2),
	(z,11,1),
	(z,11,2),
	(z,15,2),
	(z,8,3),
	(z,7,3),
	(z,5,1),
	(z,6,2),
	(z,4,1),
	(z,7,2),
	(z,6,4),
	(z,5,2),
	(z,2,1),
	(a,14,7),
	(a,14,5),
	(a,12,2),
	(a,13,2),
	(a,11,1),
	(a,12,1),
	(a,14,7),
	(a,13,5),
	(a,12,2),
	(a,13,2),
	(a,11,2),
	(a,11,1),
	(a,15,1),
	(a,9,3),
	(a,7,3),
	(a,5,1),
	(a,8,2),
	(a,14,7),
	(a,12,5),
	(a,12,2),
	(a,12,2),
	(a,11,1),
	(a,11,2),
	(a,14,7),
	(a,14,5),
	(a,12,2),
	(a,12,2),
	(a,11,1),
	(a,11,2),
	(a,15,2),
	(a,8,3),
	(a,7,3),
	(a,5,1),
	(a,6,2),
	(a,4,0),
	(a,7,2),
	(a,5,4),
	(a,5,2),
	(a,4,1),
	(a,5,1),
	(a,3,2),
	(a,5,7),
	(a,9,5),
	(a,7,4),
	(a,3,1),
	(b,14,7),
	(b,14,5),
	(b,12,2),
	(b,13,2),
	(b,11,1),
	(b,11,1),
	(b,14,7),
	(b,14,5),
	(b,12,2),
	(b,13,2),
	(b,11,1),
	(b,11,1),
	(b,15,2),
	(b,9,3),
	(b,7,4),
	(b,5,1),
	(b,6,2),
	(b,14,7),
	(b,14,5),
	(b,12,2),
	(b,13,2),
	(b,11,1),
	(b,11,1),
	(b,14,7),
	(b,14,5),
	(b,12,2),
	(b,12,2),
	(b,11,1),
	(b,11,2),
	(b,15,2),
	(b,8,3),
	(b,7,3),
	(b,5,1),
	(b,6,2),
	(b,4,1),
	(b,7,2),
	(b,6,4),
	(b,5,2),
	(b,2,1),
	(b,14,7),
	(b,14,5),
	(b,12,2),
	(b,13,2),
	(b,11,1),
	(b,12,1),
	(b,14,7),
	(b,13,5),
	(b,12,2),
	(b,13,2),
	(b,11,2),
	(b,11,1),
	(b,15,1),
	(b,9,3),
	(b,7,3),
	(b,5,1),
	(b,8,2),
	(b,14,7),
	(b,12,5),
	(b,12,2),
	(b,12,2),
	(b,11,1),
	(b,11,2),
	(b,14,7),
	(b,14,5),
	(b,12,2),
	(b,12,2),
	(b,11,1),
	(b,11,2),
	(b,15,2),
	(b,8,3),
	(b,7,3),
	(b,5,1),
	(b,6,2),
	(b,4,0),
	(b,7,2),
	(b,5,4),
	(b,5,2),
	(b,4,1),
	(b,5,1),
	(b,3,2),
	(b,5,7),
	(b,9,5),
	(b,7,4),
	(b,3,1),
	(b,5,2),
	(b,4,1)
	]
	#mycursor.execute(sqlQuery)
	#mycursor.execute(sqlQuery1)
	#myresult = mycursor.fetchall()
	#for x in myresult:
	#  print(x)
	mycursor.executemany(sql1,val1)
	mydb.commit()
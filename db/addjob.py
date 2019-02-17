import sqlite3

con = sqlite3.connect(r"e:\classroom\python\hr.db")
cur = con.cursor()
title = input("Enter job title : ")
minsal = int(input("Enter min salary : "))

cur.execute("insert into jobs(title,minsal) values(?,?)",
            (title, minsal))
con.commit()
print("Added a new job successfully!")
con.close()

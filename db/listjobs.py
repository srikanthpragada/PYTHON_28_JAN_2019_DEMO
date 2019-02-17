import sqlite3

con = sqlite3.connect(r"e:\classroom\python\hr.db")
cur = con.cursor()

cur.execute("select * from jobs order by minsal desc")
jobs = cur.fetchall()
for id, title, minsal in jobs:
    print(f"{id:3d} {title:30s} {minsal:6d}")

con.close()

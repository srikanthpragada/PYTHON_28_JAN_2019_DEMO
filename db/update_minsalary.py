import sqlite3

con = sqlite3.connect(r"e:\classroom\python\hr.db")
cur = con.cursor()
id = input("Enter job id : ")
cur.execute("select title, minsal from jobs where id = ?",(id,))
job = cur.fetchone()
if job is None:
    print("Sorry! Job id not found!")
else:
    print(f"Title = {job[0]}, Min Salary = {job[1]}")
    minsal = int(input("Enter new min salary : "))
    cur.execute("update jobs set minsal = ? where id = ?",(minsal,id))
    con.commit()
    print("Updated job successfully!")

con.close()

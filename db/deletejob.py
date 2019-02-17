import sqlite3

con = sqlite3.connect(r"e:\classroom\python\hr.db")
cur = con.cursor()
id = input("Enter job id : ")
cur.execute("delete from jobs where id = ?",(id,))
if cur.rowcount == 1:
    print("Deleted job successfully!")
    con.commit()
else:
    print("Sorry! Job id not found!")

con.close()

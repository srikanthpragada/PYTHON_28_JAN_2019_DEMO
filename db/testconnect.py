
import sqlite3


con = sqlite3.connect(r"e:\classroom\python\hr.db")
print("Connected : ", con)
con.close()

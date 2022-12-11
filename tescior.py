import sqlite3 as sql

con = sql.connect("testDb.db")

cur = con.cursor()

res = cur.execute("SELECT * FROM myTable;")

res.fetchall()
import sqlite3 as sql

con = sql.connect("testDb.db")

cur = con.cursor()

res = cur.execute("SELECT * FROM myTable")

output = res.fetchall()

print(output)

#More advanced print out

for row in output:
    print(row)
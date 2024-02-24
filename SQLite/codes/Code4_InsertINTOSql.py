# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

new_rows = [
  ('100.100.100.100', 'a.b.c', 100),
  ('200.200.200.200', 'f.d.e', 200)
]

cur.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_rows)
con.commit()

cur.execute("SELECT * FROM 'ips'")
print(cur.fetchall())
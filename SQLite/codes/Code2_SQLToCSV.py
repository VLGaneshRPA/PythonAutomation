# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import sqlite3
import pandas

# Establish a connection and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

df = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", con)
print(df)

# df.to_csv('database.csv', index=None)
df.to_excel('database.xlsx', index=None)



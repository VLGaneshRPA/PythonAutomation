# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import tabula
from tabula.io import read_pdf

#install tabula, tabula-py
#instal ARM jdk on mac, no env variable setup required, just check java -version, which java etc.,
table = tabula.read_pdf('weather.pdf', pages=1)

print(type(table[0]))

table[0].to_csv('output.csv', index=None)
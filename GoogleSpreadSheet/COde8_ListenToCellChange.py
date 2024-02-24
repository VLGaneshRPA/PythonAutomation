# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import gspread
import time

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')
worksheet2 = spreadsheet.worksheet('Watch')

#run infinitely
while True: 
  value1 = worksheet1.acell('G26').value
  print(value1, type(value1))
  time.sleep(2)
  value2 = worksheet1.acell('G26').value
  if value1 != value2:
    worksheet2.update('A1', 'CHANGED')



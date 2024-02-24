# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import gspread
import statistics

# Establish connection
gc = gspread.service_account('secrets.json')

# Get spreadsheet
spreadsheet = gc.open('weather_private') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')

# Get existing column 
existing_column = worksheet1.get_values('G2:G25')

# Flatten the existing column
existing_column = [float(i[0]) for i in existing_column]

# Calculate average and add to Worksheet
average = statistics.mean(existing_column)
worksheet1.update('G26', average)
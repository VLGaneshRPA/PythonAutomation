# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/


#Feel free to copy the data of the spreadsheeet in the link to a new spreadsheet in your Google Sheets account:
#https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/edit?usp=sharing

#downlaod secret.json from GCP > project > Google Derive > fill detail and downlaod, . Finally, enable Google Sheet APi
import gspread

gc = gspread.service_account('secrets.json')

spreadsheet = gc.open('weather_private')

# Get a worksheet by index
# worksheet1 = spreadsheet.get_worksheet(0)

# Get a worksheet by name 
worksheet1 = spreadsheet.worksheet('2013')

data = worksheet1.get_all_records()
print(data)
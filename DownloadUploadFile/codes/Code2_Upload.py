# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests

url = "https://cgi-lib.berkeley.edu/ex/fup.cgi"

file = open('input/myfile.txt', 'rb')

req = requests.post(url, files={"upfile":file})

print(req.text)
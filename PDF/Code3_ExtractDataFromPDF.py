# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import fitz
#install pip3 install fitz, frontend(if error appear)

with fitz.open("download.pdf") as pdf:
  text = ''
  for page in pdf:
    text = text + page.get_text()
    print(50*'--')  
    print(text)
    
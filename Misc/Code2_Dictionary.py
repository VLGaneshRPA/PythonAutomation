# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import json

file = open('input/data.json')
data = json.load(file)

def define(word):
  word = word.lower()
  if word in data:
    return data[word]

word = input('Please enter a word: ')
definition = define(word)
if definition:
  for item in definition:
    print(item)
else:
  print("Word was not found!")
# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

#pip install googletrans==3.1.0a0
from googletrans import Translator


translator = Translator()

translation = translator.translate('Oa mai oe?', dest='en').text

print(translation)
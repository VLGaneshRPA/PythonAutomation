# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import cv2

color = cv2.imread('tiger.jpeg', 0)
#print(color)
cv2.imwrite('tiger-gray.jpeg', color)

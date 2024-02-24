# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
  # Course URL: https://www.udemy.com/course/automate-everything-with-python/
  
import cv2

image = cv2.imread('humanswithdog.jpeg', 1)
face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)

    cv2.imwrite('humanwithdog_faces.jpeg', image)
  
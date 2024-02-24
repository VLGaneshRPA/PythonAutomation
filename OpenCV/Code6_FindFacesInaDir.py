# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
  # Course URL: https://www.udemy.com/course/automate-everything-with-python/
  
import cv2
import os
INPUT_FOLDER = 'images_input'
OUTPUT_FOLDER = 'images_output'

def findImage(imageName):
    image = cv2.imread(imageName, 1)
    face_cascade = cv2.CascadeClassifier('faces.xml')

    faces = face_cascade.detectMultiScale(image, 1.1, 4)
    print('faces',faces)
    i = 1
    for (x, y, w, h) in faces:
        
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)

    return image
  
  
images = os.listdir(INPUT_FOLDER)
for image in images:
    print(image)
    face_image = findImage(f'{INPUT_FOLDER}/{image}')
    if face_image is not None:
        cv2.imwrite(f'{OUTPUT_FOLDER}/{image}', face_image)
    
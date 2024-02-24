# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import cv2
import time

#first webcam 0
video = cv2.VideoCapture(0)
time.sleep(10)

success, frame = video.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('/Users/apple/Desktop/Python/WebScrap/VideoProcessing/input/faces.xml')
output = cv2.VideoWriter('/Users/apple/Desktop/Python/WebScrap/VideoProcessing/output/webcam_output.mp4', 
cv2.VideoWriter_fourcc(*'DIVX'), 10, (width, height))

count = 0
while success:
  faces = face_cascade.detectMultiScale(frame, 1.1, 4)
  for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)
#show video
  cv2.imshow("Recording", frame)
  key = cv2.waitKey(1)
  if key == ord('q'):
    break
  output.write(frame)
  success, frame = video.read()
  count += 1
  print(count)

output.release()
video.release()
cv2.destroyAllWindows()




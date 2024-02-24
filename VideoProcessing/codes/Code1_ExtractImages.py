# Credit: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import cv2

video = cv2.VideoCapture("/Users/apple/Desktop/Python/WebScrap/VideoProcessing/input/video.mp4")
success, frame = video.read()

count = 1
while success:
  cv2.imwrite(f'/Users/apple/Desktop/Python/WebScrap/VideoProcessing/output/{count}.jpg', frame)
  success, frame = video.read()
  count += 1
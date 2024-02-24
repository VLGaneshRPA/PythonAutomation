# Credit: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import cv2

video = cv2.VideoCapture("/Users/apple/Desktop/Python/WebScrap/VideoProcessing/input/video.mp4")
success, frame = video.read()

print(f'success :{success},  frame :{frame}')

width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
#90 images
frame_count= video.get(cv2.CAP_PROP_FRAME_COUNT)
#video time - 3sec
fps = video.get(cv2.CAP_PROP_FPS)

print(width, height, frame_count, fps)
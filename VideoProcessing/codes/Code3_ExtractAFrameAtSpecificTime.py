# Credit: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import cv2

video = cv2.VideoCapture("/Users/apple/Desktop/Python/WebScrap/VideoProcessing/input/video.mp4")
success, frame = video.read()

print(f'success :{success},  frame :{frame}')
frame_count= video.get(cv2.CAP_PROP_FRAME_COUNT)
#video time - 3sec
fps = video.get(cv2.CAP_PROP_FPS)
print('fps :',fps)

timeStamp = '00:00:02.75'
timeStamp_split = timeStamp.split(':')
timeStamp_split_float = [float(i) for i in timeStamp_split]
hours, minutes, seconds = timeStamp_split_float
print(hours, minutes, seconds,  timeStamp_split_float)


frame_nr = hours * 3600 * fps + minutes * 60 * fps + seconds * fps
print(frame_nr)

#set frame and read video
video.set(1,frame_nr)
success, frame = video.read()


cv2.imwrite(f'/Users/apple/Desktop/Python/WebScrap/VideoProcessing/output/{frame_nr}.jpg', frame)

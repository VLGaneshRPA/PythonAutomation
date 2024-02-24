# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')

beat_low = beat.low_pass_filter(2000)
beat_low.export('beat_low.wav')

beat_left = beat_low.pan(-1)
beat_right = beat_low.pan(1)

beat_final = beat_left + beat_right + beat_low
beat_final.export('beat_final.wav')


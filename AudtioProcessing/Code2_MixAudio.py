# Author: Ganesh.vl, https://www.linkedin.com/in/sas-rpaautomation/ 
 # Credit: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')
sax = AudioSegment.from_wav('sax.wav')

print(len(beat), len(sax))

beat2 = beat * 2
beat2.export('beat2.wav')

mixed = beat2.overlay(sax)
mixed.export('mixed.wav')

final = beat2 + mixed * 2 + sax + beat2 + sax
final.export('final.wav')



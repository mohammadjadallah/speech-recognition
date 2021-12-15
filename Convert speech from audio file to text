# In this code you will be able make simple program to convert the speech to text
# This will convert speech that discussion from the recorded file to text
# pip install SpeechRecognition
# we will use two library SpeechRecognition and os
# os we will use it to check whether exist content inside the file or not
# pip install pyaudio even if you have problem
'''

python..
conditions(if esle)
with statement
    try:
    except:
text To file
open('namefile.txt','w')

'''


import speech_recognition as talk
import os

recognize = talk.Recognizer()
path = 'speech.wav' # just put the path you want

if os.stat(path).st_size == 0:
    print('This is empty file')
else:
    with talk.AudioFile(path) as source:
        try:
            audio = recognize.record(source)
            saveFile = open('speechToText.txt', 'w') # this to save the text in text file
            print(recognize.recognize_google(audio), file=saveFile)
        except talk.UnknownValueError:
            print('try another file')

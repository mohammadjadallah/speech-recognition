# Let's make the computer talk 😅
# How we can convert the text to speech
# here we made a simple program that allow to user choose man or woman to talk 
#pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()
gender = input('what do you want to talk male or female? ')
say =  input("What do you want say: ")
voice = engine.getProperty('voices')
engine.setProperty("rate", 120) # 120 The best
if gender == 'female':
    engine.setProperty('voice',voice[1].id) # 1 this will be woman
    engine.say(say)
    engine.runAndWait()

elif gender == 'male':
    engine.setProperty('voice', voice[0].id) # 0 this will be man
    engine.say(say)
    engine.runAndWait()



'''
if we want to know what is the rate we can use getProperty() and put 'rate'
rate is how do you want to the speacker talk fast or slowly
rate = engine.getProperty("rate")
print(rate)

and you can sellect the rate about way setProperty('rate', 'value you want like 120')
sellectRate = engine.setProperty("rate")
print(sellectRate)

and we can use setProperty to sellect volume and gender male or female
engine.setProperty('volume', 2.7)
'''

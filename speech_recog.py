#! /usr/bin/python -tt
import os
import speech_recognition as sr

def main():
  print "hello starting the program now!"
  re = sr.Recognizer()
  with sr.Microphone() as source:
    print 'Say something buddy:'
    audio = re.listen(source)
  
#  try to recognize using google
#  try:
#    APIkey = os.environ["key"]
#    print APIkey
#    print 'Google thinks that you said: ', re.recognize_google(audio, APIkey)
#    print 'google thinks that you said: ', re.recognize_google(audio)
#  except sr.UnknownValueError:
#    print "Google did not understand what you just said"
#  except sr.RequestError as e:
#    print "Could not request result from Google's speech recognition API", format(e)

#  try to recognize using bing
  BING_KEY = os.environ["bing_key"]
  try:
    print 'Bing speech recognition thinks you said:', re.recognize_bing(audio, key=BING_KEY)
  except sr.UnknownValueError:
   print "Bing did not understand what you just said"
  except sr.RequestError as e:
    print "Could not request result from Bing's speech recognition API", format(e)
    
if __name__ == '__main__':
  main()




import pyttsx3
engine = pyttsx3.init()

volume = engine.getProperty('volume')   
print (volume)                         
engine.setProperty('volume',1.0) 

rate = engine.getProperty('rate')   
print (rate)                        
engine.setProperty('rate', 160)     



print("loading please wait....")
engine.say("hello master suraj  how can i help you i am jarvis your new assistant")
engine.runAndWait()
#by Nicholas Scarpa & Rishabh Prasad
#using python version 3.6.2
import speech_recognition as sr
#pip install SpeechRecognition
#pip install PyAudio
import webbrowser
import smtplib
import datetime
import getpass

def sendEmail(to, content, userEmail, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(userEmail, password)
    server.sendmail(userEmail, to, content)
    server.close()
    
def takeCommand():
    startStop = True
 
    while startStop:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            listener.pause_threshold = 1
            voice = listener.listen(source) 
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'holmes' in command and 'open google' in command or 'open google' in command:
                #say "open google"s 
                print('Okay sir, opening google...')
                webbrowser.open('google.com')
            elif 'holmes' in command and 'open youtube' in command or 'open youtube' in command:
                #say "open youtube"
                print('Okay sir, opening youtube...')
                webbrowser.open('youtube.com')
            elif 'holmes' in command and 'open future hacks' in command or 'open future hacks' in command:
                #say "future hacks"
                print('Okay sir, opening Devpost')
                webbrowser.open('https://futurehacks-2021.devpost.com/?ref_feature=challenge&ref_medium=discover')
            elif 'holmes' in command and 'the time' in command or 'the time' in command:
                #say "what is the time"
                Time = datetime.datetime.now().strftime("%I:%M:%S")
                print("Sir, the current time is " + Time)
            elif 'holmes' in command and 'the date' in command or 'the date' in command:
                #say "what is the date"
                year = str(datetime.datetime.now().year)
                month = str(datetime.datetime.now().month)
                day = str(datetime.datetime.now().day)
                print("Sir, the date is, " + month + "/" +  day + "/" + year)
            elif 'holmes' in command and 'send email' in command or 'send email' in command: 
                #say "send email"
                try:
                    userEmail = input('Enter your email: ')
                    password = getpass.getpass('What is your password: ')
                    emailTo = input('Enter the email you want to send to: ')
                    print('What should I say?')
                    voice2 = listener.listen(source) 
                    query = listener.recognize_google(voice2)
                    content = query
                    to = emailTo
                    print('Okay sir, sending email...')
                    sendEmail(to, content, userEmail, password)
                    print('Email sent!') 
                except Exception as e:
                    print(e)
                    print('Sorry sir, I was unable to send that email')
            elif 'bye holmes' in command or 'goodbye' in command:
                print('Bye, sir')
                startStop = False
            elif 'hey holmes' in command or 'hello' in command:
                print('Hello, sir. How may I help you?')
            else: 
                print('Recognizing...')
                print('Sorry, I could not understand that. Can you repeat it?')
 
if __name__ == "__main__":
    password = 'fly on rainbows'
    test = input('Finish the sentence. Pink kittens ')
    if test == password:
        numLock = '5344'
        test2 = input('Enter the password for the 4 digit number lock: ')
        if test2 == numLock:
            print('Holmes has been accessed.')
            print('Hello sir. How can I help you?')
            takeCommand()
        else: print('Permission Denied')
    else:
        print('Permission Denied')

# Speech Synthesis####


import pyttsx3
import tkinter as tkr
import pyaudio
import speech_recognition as sr

app = tkr.Tk()
app.geometry('500x500')
app.title('Chatbot')


def textToSpeech(x):
    ssynth = pyttsx3.init()
    ssynth.setProperty('Rate',0.1)
    ssynth.say(x)
    ssynth.runAndWait()


tkr.Label(app,text="",font=('Arial',10)).pack()
tkr.Label(app,text="Text to Speech",font=('Arial',25)).pack()
tkr.Label(app,text="",font=('Arial',10)).pack()

textInput = tkr.Variable(app)
tkr.Entry(app,textvariable= textInput,font=(30),width=40).pack()

tkr.Label(app,text="",font=('Arial',10)).pack()

Btn = tkr.Variable(app)
tkr.Button(app,text='Speak',command = lambda:textToSpeech(textInput.get())).pack()
tkr.Label(app,text="",font=('Arial',10)).pack()

tkr.Label(app,text="_____________________________________",font=('Arial',10),fg="grey").pack()


tkr.Label(app,text="",font=('Arial',10)).pack()

### Speech to Text

def speechToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Say Something')
        audio = r.listen(source)
        spText = r.recognize_google(audio)
        print('You Said >>' , spText)
        tkr.Label(app,text="",font=('Arial',10)).pack()
        tkr.Label(app,text=spText,font=('Arial',20),fg="red").pack()


tkr.Label(app,text="Speech to Text",font=('Arial',25)).pack()
tkr.Label(app,text="",font=('Arial',10)).pack()
Btn = tkr.Variable(app)
tkr.Button(app,text="Listen",command =lambda :speechToText()).pack()


app.mainloop()




    

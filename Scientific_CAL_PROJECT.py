import tkinter as tkr
from tkinter import StringVar
app = tkr.Tk()
app.title('Kelsi')
app.geometry('400x480')
app.maxsize(width=400,height=500)
app.minsize(width=400,height=500)
app.configure(background="#333333")
xpath = [50,135,215,295]
ypath = [180,250,320,390]
btnList= [7,8,9,"/",4,5,6,"*",1,2,3,'-','C',0,'=','+']    
expression = ''
resultString = StringVar()

res = tkr.Variable(app)
resultString.set("0")
tkr.Label(app,text=res.get(),font=('Comic Sans',25),width=14,height=2
          ,relief="raised",
          textvariable=resultString,bg='#333333',fg='white').place(x=50,y=50)

def equalto():
    global expression
    if expression != '':
        total = str(eval(expression))
        resultString.set(total)
        expression = ''

def clear():
    global expression
    resultString.set(0)
    expression = ""

def showprocess(btnNO):
    if btnNO == "=":
        equalto()
    elif btnNO == "C":
        clear()
    else:    
        global expression
        expression = expression + str(btnNO)
        resultString.set(expression)
    
def viewButtons(number,xplace,yplace):
       for i in btnList:
            tkr.Button(app,text=number,bg = '#1f1f1f',
                       justify="center",fg = 'white',font=('Arial',25)
                       ,width=1,height=1,borderwidth=0,
                       relief="ridge",activeforeground="#1f1f1f",
                   activebackground="white",
            command=lambda:showprocess(number)).place(x=xplace,y=yplace)

number = 0
for i in ypath:
    for j in xpath:
        viewButtons(btnList[number],j,i)
        number += 1

app.mainloop()


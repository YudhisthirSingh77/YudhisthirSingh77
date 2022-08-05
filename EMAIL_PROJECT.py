import tkinter as tkr
from tkinter import ttk
from tkinter import messagebox
import tkinter.filedialog as tkfd
import smtplib
import imghdr
from email.message import EmailMessage
import imap_tools
from imap_tools import MailBox



app = tkr.Tk()
app.geometry('1000x800')
app.title('EmailApp')

##def show():
##    print('')
with MailBox('imap.gmail.com').login('yudhisthir1998@gmail.com','pass','INBOX') as mailbox:
    bodies = [msg.text or msg.html for msg in mailbox.fetch()]

###Mail_list###
selected = ""
lb = tkr.Variable(app)
mail_box = tkr.Listbox(app,width=30,height=600,activestyle='dotbox',fg='white',bg='black')
mail_list = ['yudhisthir1998@gmail.com' ,'yudhisthirsingh579@gmail.com']

for i in mail_list:
    mail_box.insert(tkr.END,i)
mail_box.select_set(0)
curs = mail_box.curselection
mail_box.place(x=0,y=0)


msg_box = tkr.Listbox(app , width=30, height=600,activestyle='dotbox',fg='white',bg='black')

for i in range(10):
    msg_box.insert(tkr.END,bodies[i])
msg_box.select_set(0)
curs = msg_box.curselection
msg_box.place(x=600,y=10)

    
###label###

tkr.Label(app,text='To:',font=('Arial',18),fg='black').place(x=340,y=50)
tkr.Label(app,text='Sub:',font=('Arial',18),fg='black').place(x=340,y=100)
tkr.Label(app,text='Msg:',font=('Arial',18),fg='black').place(x=340,y=150)


##Entry###

toEnt = tkr.Variable(app)
toEnt.set(mail_box.get(curs()))
tkr.Entry(app,textvariable=toEnt,font=(20),width=25).place(x=300,y=55)

SubEnt = tkr.Variable(app)
tkr.Entry(app,textvariable=SubEnt,font=(20),width=25).place(x=300,y=105)

msgEnt = tkr.Variable(app)
tkr.Entry(app,textvariable=msgEnt,font=(20),width=25).place(x=300,y=155)


#######
def addAttachment():
    with open('demo.txt','rb') as f1:
        file_data = f1.read()
        file_type = imghdr.what(f1.name)
        file_name = f1.name

###attachment###

def attach():
    global img
    file = tkfd.askopenfiles(mode='r',filetypes=[('Images','*.jpeg')])
    print(file)
    Img_name =file[0].name
    img1 = Image.open(Img_name)
    img1 = img1.resize((200,200))
    img = ImageTk.PhotoImage(img1)

    if img != null:
        addAttachment()

##EmailMessage####
def sendMail():
    toEnt.set(mail_box.get(curs()))

    msg = EmailMessage()
    msg['To'] = toEnt.get()
    msg['Subject'] = SubEnt.get()
    msg['from'] = 'yudhister@gmail.com'
    msg.set_content(msgEnt.get())
    msg.add_attachment(file_data,maintype='application',subtype='octet_stream',filename=file_name)
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('yudhister@gmail.com','pass')
    server.send_message(msg)
    server.quit()

tkr.Button(app,text='attach',command=attach,bg='lightblue').place(x=450,y=300)
tkr.Button(app,text='Send',command=sendMail,bg='green').place(x=600,y=300)


### inbox ###



 






##app.mailloop()




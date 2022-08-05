import smtplib
import imghdr
from email.message import EmailMessage
import imap_tools
from imap_tools import MailBox


print('Select Option \n1 Inbox \n2 Compose Mail\n')
v = input('')

def inbox():
    with MailBox('imap.gmail.com').login('yudhisthir1998@gmail.com','pass','INBOX') as mailbox:
        bodies = [msg.text or msg.html for msg in mailbox.fetch()]
    print('printtt')
def mail():
    pass

def options(v):
    if v == '1':inbox()
    elif v =='2' :mail()
        
options(v)

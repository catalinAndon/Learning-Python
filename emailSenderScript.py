# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import ttk
import smtplib,ssl, email
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

background = 'gray25'
foreground = 'snow'
sender = 'catalin.andon.84.gl@gmail.com'
password = 'andreea123'

#send mail function-----------------------------------------------------------------------------------------------------

def sendMail(reciver, message):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender,password)
    s.sendmail(sender,reciver,message)
    s.quit()

#e-mail address check function-----------------------------------------------------------------------------------------------------

def emailSyntaxVerify():
             emailAddress= reciverAddress.get()
             match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)
             if match == None :
                 messagebox.showerror("Bad syntax","Wrong typed E-mail Address!",icon = 'error')
                 raise ValueError('Bad Syntax')
             else:
                 sendMail(reciverAddress.get(), msg.get("1.0",END))


# GUI code using Tkinter module -----------------------------------------------------------------------------------------------------

root = Tk()
root.geometry('700x500')
root.configure(background=background)
root.title('MailSenderScript')
Label(root, text="Send Email",font=('',30),foreground = foreground, background = background).place(x=200, y=10)


#CC Entry widget -----------------------------------------------------------------------------------------------------

Label(root,text = "Cc:",font = ('',20), foreground = foreground, background = background).place(x=10, y=108)
cc = Entry(root,font =('',17),width =30)
cc.place(x = 140,y=109)


#Text message-widget -----------------------------------------------------------------------------------------------------

Label(root,text = "Send to:",font = ('',20), foreground = foreground, background = background).place(x=10, y=70)
reciverAddress = Entry(root,font = ('',17), width=30)
reciverAddress.place(x=140,y=70)


Label(root,text = "Subject:",font = ('',20), foreground = foreground, background = background).place(x=10, y=149)
subject=Entry(root,font =('',17),width =30)
subject.place(x = 140,y=149)


#text box/entry widget -----------------------------------------------------------------------------------------------------

Label(root,text = "Message:",font = ('',20), foreground = foreground, background = background).place(x=10, y=200)
msg=Text(root, height=7, width=30,font=('',17))
msg.insert(INSERT,subject.get())
msg.place(x=140,y=200)



#scrollbar widged , asociated with Text-----------------------------------------------------------------------------------------------------

scrollbar = ttk.Scrollbar(root,orient='vertical' ,command =msg.yview)
scrollbar.place(x=550, y=201)
msg['yscrollcommand']=scrollbar.set

#button widget-----------------------------------------------------------------------------------------------------

Button(root, text = "Send",font = ('',20),foreground='gray25', command = lambda:emailSyntaxVerify()).place(x=310,y=420)
root.mainloop()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
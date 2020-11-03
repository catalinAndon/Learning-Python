# -*- coding: utf-8 -*-

import smtplib
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext

background = '#f1c159'
foreground = '#2b2b2b'
sender = 'catalin.andon.84.gl@gmail.com'
password = 'andreea123'

#send mail function

def sendMail(reciver, message,cc,fetch):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender,password)
    s.sendmail(sender,reciver,message)
    s.quit()
    
# Fetch scrolltext() value to string method . 

def fetchTxt():
    global msg,txt    
    fetch=msg.get('1.0','end-1c')
    txt['msg']="" + fetch
    print (txt)

    
# GUI code using Tkinter module 


root = Tk()
root.geometry('700x450')
root.configure(background=background)
root.title('MailSenderScript')
txt=Label(root).place(x=250, y=10)
Label(root, text="Email Sender",font=('',30),foreground = foreground, background = background).place(x=200, y=10)
Label(root,text = "Send to:",font = ('',20), foreground = foreground, background = background).place(x=10, y=70)
Label(root,text = "Cc:",font = ('',20), foreground = foreground, background = background).place(x=10, y=108)
cc = Entry(root,font =('',17),width =30)
cc.place(x = 140,y=109)
Label(root,text = "Message:",font = ('',20), foreground = foreground, background = background).place(x=10, y=150)

#name Entry 
name = Entry(root,font = ('',17), width=30)
name.place(x=140,y=70)


#message Entry 
msg = scrolledtext.ScrolledText(root, wrap = 'word', width=51, height=10, font=("Times New Roman",12))
msg.grid(column=10,pady=160,padx=140)
msg.focus()
 
    
Button(root, text = "Send",font = ('',20),foreground=foreground, command = lambda:sendMail(name.get(),cc.get(),msg.get('1.0','end-1c'),fetchTxt)).place(x=310,y=380)
root.mainloop()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
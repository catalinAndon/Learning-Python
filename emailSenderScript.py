# -*- coding: utf-8 -*-

import smtplib
from tkinter import *

background = '#f1c159'
foreground = '#2b2b2b'
sender = 'catalin.andon.84.gl@gmail.com'
password = 'andreea123'

#send mail function

def sendMail(reciver, message):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender,password)
    s.sendmail(sender,reciver,message)
    s.quit()

# GUI code using Tkinter module 

root = Tk()
root.geometry('700x450')
root.configure(background=background)
root.title('MailSenderScript')
Label(root, text="Email Sender",font=('',30),foreground = foreground, background = background).place(x=200, y=10)
Label(root,text = "Send to:",font = ('',20), foreground = foreground, background = background).place(x=10, y=70)
Label(root,text = "Cc:",font = ('',20), foreground = foreground, background = background).place(x=10, y=108)
cc = Entry(root,font =('',17),width =30)
cc.place(x = 140,y=109)
Label(root,text = "Message:",font = ('',20), foreground = foreground, background = background).place(x=10, y=150)
name = Entry(root,font = ('',17), width=30)
name.place(x=140,y=70)
msg=Text(root, height=7, width=30,font=('',17))
msg.place(x=140,y=150)
Button(root, text = "Send",font = ('',20),foreground=foreground, command = lambda:sendMail(name.get(),msg.get("1.0",END))).place(x=310,y=380)
root.mainloop()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
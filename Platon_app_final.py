# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 23:21:40 2020

@author: catal
"""

import tkinter as tk
import csv
import re
import datetime
import time
from collections import Counter
from tkinter import Tk, RIGHT, RAISED,Text, TOP, BOTH, X, N, LEFT
from tkinter import *
from tkinter.ttk import Frame, Button, Style,Label,Entry
from tkinter import ttk
from tkinter.messagebox import showinfo
#import MySQLdb,random,os



class PlatonApp(tk.Tk):
    def __init__(self):
        tk.Tk. __init__(self)
        self._frame= None
        self.switch_frame(mainWindow)
        
        
        
    def switch_frame(self,frame_class):
        new_frame=frame_class(self)
        if self._frame is not None :
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()



class mainWindow(tk.Frame):
    def __init__(self,master):                
        tk.Frame.__init__(self,master)
        self.master.title("PLATON")
        #self.master.pack(fill=BOTH, expand = 1)
        self.master.geometry("350x300+350+300")
        
              
           
        
 #variables declaration  
              
        
        password1 = StringVar()
        username = StringVar()
                
 #Username label & Entry  
                
        frame1 = tk.Frame(self, background="#333")
        frame1.pack(fill=X)
        self.pack(fill=BOTH, expand=True)
        label1=Label(frame1,text=" ", background="#333").pack()
        label2=Label(frame1,text="Login Window: ",width=15,background="#333",foreground="white",anchor="center",font = ("Courier",14,"bold")).pack()
        label3=Label(frame1,text=" ",background="#333").pack()
        label4=Label(frame1,text="Username :",width=12,background="#333",foreground="white")
        label4.pack(side=LEFT,padx=5,pady=5)
        entry1 = tk.Entry (frame1,fg = "#333",font = ("bold"))
        entry1.configure(textvariable = username)
        entry1.pack(fill=X,padx=5,expand=True)
        
       
#password Label & Entry 
        
        frame2 =tk.Frame(self, background="#333")
        frame2.pack(fill=X)
        self.pack(fill=BOTH, expand=True)
        label5 = Label(frame2, text="Password :", width=12,foreground="white",background="#333")
        label5.pack(side=LEFT, padx=5, pady=5)
        entry2 =tk. Entry(frame2,fg = "#333",font = ("bold"))
        entry2.configure(textvariable = password1, show="*")
        entry2.pack(fill=X, padx=5, expand=True)
        
        
#Buttons 
        
        #Login button
        
        frame3 = tk.Frame(self, background="#333")
        frame3.pack(fill=X)
        label6=Label(frame3,text=" ",background="#333").pack()
        button1=tk.Button(frame3,text="LogIn",font=("Calibri", 10),height ="1", width="10",padx=0, pady=0,)
        button1.pack()
        
        
        #Register button
        
        frame4 = tk.Frame(self, background="#333")
        frame4.pack(fill=X)
        label7=Label(frame4,text=" ",background="#333").pack()
        button2=tk.Button(frame4,text="Register",font=("Calibri", 10),height ="1", width="10",padx=0, pady=0,command = lambda:master.switch_frame(registerWindow))
        #button2.configure(command = lambda:master.switch_frame(registerWindow))
        button2.pack()
        label8=Label(frame4,text=" ",background="#333").pack()
        label9=Label(frame4,text=" ",background="#333").pack()
        label10=Label(frame4,text=" ",background="#333",font = ("Courier",40,"bold")).pack()
        
class registerWindow(tk.Frame):

   def __init__(self,master):
                
        tk.Frame.__init__(self,master)
        self.master.title("PLATON")
        #self.master.pack(fill=BOTH, expand = 1)
        self.master.geometry("350x300+350+300")
        
        
#Variables declaration    
        
        full_name = tk.StringVar()
        email1 = tk.StringVar()
        password2 = tk.StringVar()
        password3 = tk.StringVar()
        
#date and time method
        
        dateTime = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        
        
            
        
#save info to .csv method
        
        with open('DataBase.csv','a') as csvfile:
                    fieldnames=('Name','E_mail','Password','PasswordConfirm','Date&Time')
                    writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
                    writer.writeheader()
                     
            
        def saveOutput (self,master):
            with open ('DataBase.csv','a') as csv_save:
                    writer=csv.DictWriter(csv_save, fieldnames=fieldnames)
                    writer.writerow({'Name': full_name.get(), 'E_mail':email1.get(), 'Password':password2.get(), 'PasswordConfirm':password3.get(),'Date&Time':dateTime})
               
                
                     
                
        def emailSyntaxVerify(self,master):
             emailAddress= email1.get()
             match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailAddress)
             if match == None :
                 messagebox.showerror("Bad syntax","Wrong typed E-mail Address!",icon = 'error')
                 raise ValueError('Bad Syntax')
                 
             else: 
                    passwordCompare(self,master)
                     
              
        def passwordCompare (self,master):            
           p1 = password2.get()
           p2 = password3.get()
                     
           if Counter(p1)==Counter(p2):
              progress_barr(self,master)
              saveOutput(self,master)
              messagebox.showinfo("Please login","Your account has been created !",icon = 'info')
              master.switch_frame(mainWindow)
               
           else:
                   progress_barr(self,master)
                   messagebox.showerror("Error","Passwords don`t match!",icon = 'error')
             
             
             
#Labels and entries for name, email, password, password confirmation
        
                
#full name entry and label
        frame1 = tk.Frame(self,background="#333")
        frame1.pack(fill = X)
        self.pack(fill=BOTH, expand=False)  
        
        #label1=tk.Label(frame1,text=" ",background="#333").pack()
        label2=tk.Label(frame1,text="Register Window: ",width=17,background="#333",foreground="white",anchor="center",font = ("Courier",14,"bold")).pack()
        label3=tk.Label(frame1,text=" ",background="#333").pack()
        label4=tk.Label(frame1,text="Full Name :",width=12,background="#333",foreground="white")
        label4.pack(side=LEFT,padx=5,pady=5)
        entry1 = tk.Entry(frame1)
        entry1.configure(textvariable = full_name)
        entry1.pack(fill=X,padx=5,expand=True)
        
#e-mail entry and label    
        
        frame2 = tk.Frame(self,background="#333")
        frame2.pack(fill = X)
        self.pack(fill=BOTH, expand=False) 
        label5=tk.Label(frame2,text=" ",background="#333",font = ("Courier",1,"bold")).pack()
        label6=tk.Label(frame2,text="Email :",width=12,background="#333",foreground="white")
        label6.pack(side=LEFT,padx=5,pady=5)
        entry2 = tk.Entry(frame2)
        entry2.configure(textvariable = email1)
        entry2.pack(fill=X,padx=5,expand=True)
        
 #password entry and label 
        
        frame3 = tk.Frame(self,background = "#333")
        frame3.pack(fill = X)
        self.pack(fill=BOTH,expand = False)
        label7=tk.Label(frame3,text=" ",background="#333",font = ("Courier",1,"bold")).pack()
        label8=tk.Label(frame3,text="Password :",width=12,background="#333",foreground="white")
        label8.pack(side=LEFT,padx=5,pady=5)
        entry3 = tk.Entry(frame3)
        entry3.configure(textvariable = password2,show="*")
        entry3.pack(fill=X,padx=5,expand=True)
        
        
        
# Confirm password
        
        frame4 = tk.Frame(self,background = "#333")
        frame4.pack(fill = X)
        self.pack(fill=BOTH,expand = False)
        label9=tk.Label(frame4,text=" ",background="#333",font = ("Courier",1,"bold")).pack()
        label10=tk.Label(frame4,text="Confirm Pass :",width=12,background="#333",foreground="white")
        label10.pack(side=LEFT,padx=5,pady=5)
        entry4 = tk.Entry(frame4)
        entry4.configure(textvariable = password3,show="*")
        entry4.pack(fill=X,padx=5,expand=True)
        
#submit button 
        
        frame5 = tk.Frame(self,background = "#333")
        frame5.pack(fill = X)
        self.pack(fill=BOTH,expand = False)
        label11=tk.Label(frame5,text=" ",background="#333",font = ("Courier",1,"bold")).pack()
        button1=tk.Button(frame5,text="Submit",font=("Calibri", 10),height ="1", width="10",padx=0, pady=0,command = lambda:[emailSyntaxVerify(self,master)])
        button1.pack()
        
 #progress bar function 
        
        frame6 = tk.Frame(self,background = "#333")
        frame6.pack(fill = X)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar",troughcolor = '#333',background='white',bordercolor = '#333')            
        progress=ttk.Progressbar(frame6,style="red.Horizontal.TProgressbar",orient = HORIZONTAL,length = 100,mode = 'determinate')
                                
        def progress_barr(self,master):
             
             progress ['value']=20
             master.update_idletasks()
             time.sleep(1)
             
             progress['value'] = 40
             master.update_idletasks() 
             time.sleep(1)
 
             progress['value'] = 40
             master.update_idletasks() 
             time.sleep(1)
             
             progress['value'] = 60
             master.update_idletasks() 
             time.sleep(1)
             
             progress['value'] = 80
             master.update_idletasks() 
             time.sleep(1)
             
             progress['value'] = 100
             master.update_idletasks() 
             time.sleep(1)
        progress.pack(pady=10)
             
             
             
#fill frame 
        frame7 = tk.Frame(self,background = "#333")
        frame7.pack(fill = X)
        self.pack(fill=BOTH,expand = False)
        label12=tk.Label(frame7,text=" ",background="#333",font = ("Courier",20,"bold")).pack()
        
        

if __name__ == '__main__':
    app = PlatonApp()
    app.mainloop()

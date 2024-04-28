from tkinter import *
from functools import partial
import os
tkWindow = Tk()

def validateLogin(username, password):
        if((username.get() == "admin") and  (password.get()=="123")):
                print("login sucessful")
                tkWindow.destroy()
                os.system('python currency-detection.py')
        else:
                print("login failed")
                T = Text(tkWindow, height = 5, width = 52)
                l = Label(tkWindow, text = "Failed LOGIN").grid(row=6, column=0)
                l.config(font =("Courier", 14))
        return

  
tkWindow.geometry('400x150')  
tkWindow.title('Fake Currency login From')
tkWindow.configure(bg='lightgreen')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()

from tkinter import *
from tkinter import messagebox

# main root
root=Tk()
root.title('For My Love')
root.iconbitmap('C:\\Users\\Windows\\Desktop\\project\\for my love\\icons\mainroot.ico')
root.resizable(width=False, height=False)

# my root's geometry
w=500
h=500
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
x=(sw/2)-(w/2)
y=(sh/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w,h, x, y))

# name entry part
nameLabel=Label(master=root, text='name: ')
nameLabel.pack()
nameEntry=Entry(master=root)
nameEntry.pack()

# password entry part
passLabel=Label(master=root, text='password: ')
passLabel.pack()
passEntry=Entry(master=root)
passEntry.pack()

# my name and password control
name='GUMBULI'
password='1226'
def nameAndPassControl(event):
    if nameEntry.get().upper() != name.upper():
        messagebox.showerror('Error happend', 'name isn\'t correct')
    elif passEntry.get().upper() != password.upper():
        messagebox.showerror('Error happend', 'password isn\'t correct')
        

# submit button part
nameButton=Button(master=root, text='submit', bg='#F0F0F0')
nameButton.pack()
nameButton.bind('<Enter>',lambda event: nameButton.config(bg='#888888'))
nameButton.bind('<Leave>',lambda event: nameButton.config(bg='#F0F0F0'))
nameButton.bind('<Button>',nameAndPassControl)

  
# setting part
def settingButton(event):
    def secControl():
        def changeDestroy(event):
            global name, password
            name=newNameEntry.get()
            password=newpassEntry.get()
            securityRoot.destroy()
            settingRoot.destroy()
        if secEntry.get()=='1226':
            # my setting root
            settingRoot=Tk()
            settingRoot.title('setting')
            settingRoot.iconbitmap('C:\\Users\\Windows\\Desktop\\project\\for my love\\icons\setting.ico')
            w=300
            h=300
            x=(sw/2)-(w/2)
            y=(sh/2)-(h/2)
            settingRoot.geometry('%dx%d+%d+%d'%(w,h, x, y))
            
            newNameLabel=Label(master=settingRoot, text='new name:  ')
            newNameLabel.pack()
            
            newNameEntry=Entry(master=settingRoot)
            newNameEntry.pack()
            
            newpassLabel=Label(master=settingRoot, text='new password:  ')
            newpassLabel.pack()
            
            newpassEntry=Entry(master=settingRoot)
            newpassEntry.pack()
            
            okButton=Button(master=settingRoot, text='apply', bg='#F0F0F0')
            okButton.bind('<Enter>', lambda event: okButton.config(bg='#888888'))
            okButton.bind('<Leave>', lambda event: okButton.config(bg='#F0F0F0'))
            okButton.bind('<Button>', changeDestroy)
            okButton.pack()            
            
            settingRoot.mainloop()
        else:
            messagebox.showerror('security', 'password isn\'t correct')

    # my security part
    securityRoot=Tk()
    securityRoot
    securityRoot.title('security')
    securityRoot.iconbitmap('C:\\Users\\Windows\\Desktop\\project\\for my love\\icons\security.ico')
    w=250
    h=250
    x=(sw/2)-(w/2)
    y=(sh/2)-(h/2)
    securityRoot.geometry('%dx%d+%d+%d'%(w,h, x, y))
    
    secLabel=Label(master=securityRoot, text='password: ')
    secLabel.pack()
    
    secEntry=Entry(master=securityRoot)
    secEntry.pack()
        
    secButton=Button(master=securityRoot,text='confirm', bg='#F0F0F0', command=secControl)
    secButton.bind('<Enter>', lambda event: secButton.config(bg='#888888'))
    secButton.bind('<Leave>', lambda event: secButton.config(bg='#F0F0F0'))
    secButton.pack()
    securityRoot.mainloop()
        

        
# setting button
setButton=Button(master=root, text='setting', bg='#F0F0F0')
setButton.pack(side="bottom")
setButton.bind('<Enter>',lambda event: setButton.config(bg='#888888'))
setButton.bind('<Leave>',lambda event: setButton.config(bg='#F0F0F0'))
setButton.bind('<Button>',settingButton)


# exit button
exitButton=Button(master=root, text='Exit', bg='#F0F0F0')
exitButton.pack()
exitButton.bind('<Enter>',lambda event: exitButton.config(bg='#888888'))
exitButton.bind('<Leave>',lambda event: exitButton.config(bg='#F0F0F0'))
exitButton.bind('<Button>',lambda event: root.destroy() if messagebox.askokcancel('Quit', 'do you want to exit?') else 5)



root.mainloop()

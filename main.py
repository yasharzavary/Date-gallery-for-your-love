from tkinter import *
from tkinter import messagebox
from PIL import Image

# main root
root=Tk()
root.title('For My Love')
root.iconbitmap('icons\mainroot.ico')
root.resizable(width=False, height=False)

# my root's geometry
w=500
h=500
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
x=(sw/2)-(w/2)
y=(sh/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w, h, x, y))

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
    else:
        def imageShow(event):
            im=Image.open("photos\\"+event.widget.cget("text")+".png")
            im.show()
        dataroot=Tk()
        dataroot.title('MY LOVE')
        dataroot.iconbitmap('icons\\love.ico')
        w=500
        h=500
        x=(sw/2)-(w/2)
        y=(sh/2)-(h/2)
        dataroot.geometry('%dx%d+%d+%d'%(w, h, x, y))
        
        date1Button=Button(master=dataroot, text='1402-02-23',bg='#F0F0F0')
        date1Button.bind('<Enter>', lambda event: date1Button.config(bg='#888888'))
        date1Button.bind('<Leave>', lambda event: date1Button.config(bg='#F0F0F0'))
        date1Button.bind('<Button>', imageShow)
        date1Button.pack(anchor="nw")
        
        date2Button=Button(master=dataroot, text='1402-02-25',bg='#F0F0F0')
        date2Button.bind('<Enter>', lambda event: date2Button.config(bg='#888888'))
        date2Button.bind('<Leave>', lambda event: date2Button.config(bg='#F0F0F0'))
        date2Button.bind('<Button>', imageShow)
        date2Button.pack(anchor="ne")
        
        date3Button=Button(master=dataroot, text='1401-12-25',bg='#F0F0F0')
        date3Button.bind('<Enter>', lambda event: date3Button.config(bg='#888888'))
        date3Button.bind('<Leave>', lambda event: date3Button.config(bg='#F0F0F0'))
        date3Button.bind('<Button>', imageShow)
        date3Button.pack(anchor="nw")
        
        date4Button=Button(master=dataroot, text='1401-05-01',bg='#F0F0F0')
        date4Button.bind('<Enter>', lambda event: date4Button.config(bg='#888888'))
        date4Button.bind('<Leave>', lambda event: date4Button.config(bg='#F0F0F0'))
        date4Button.bind('<Button>', imageShow)
        date4Button.pack(anchor="ne")
        
        date5Button=Button(master=dataroot, text='1401-06-13',bg='#F0F0F0')
        date5Button.bind('<Enter>', lambda event: date5Button.config(bg='#888888'))
        date5Button.bind('<Leave>', lambda event: date5Button.config(bg='#F0F0F0'))
        date5Button.bind('<Button>', imageShow)
        date5Button.pack(anchor="nw")
        
        date6Button=Button(master=dataroot, text='1401-03-02',bg='#F0F0F0')
        date6Button.bind('<Enter>', lambda event: date6Button.config(bg='#888888'))
        date6Button.bind('<Leave>', lambda event: date6Button.config(bg='#F0F0F0'))
        date6Button.bind('<Button>', imageShow)
        date6Button.pack(anchor="ne")
        
        date7Button=Button(master=dataroot, text='1401-05-19',bg='#F0F0F0')
        date7Button.bind('<Enter>', lambda event: date7Button.config(bg='#888888'))
        date7Button.bind('<Leave>', lambda event: date7Button.config(bg='#F0F0F0'))
        date7Button.bind('<Button>', imageShow)
        date7Button.pack(anchor="nw")
        
        date8Button=Button(master=dataroot, text='1401-05-18',bg='#F0F0F0')
        date8Button.bind('<Enter>', lambda event: date8Button.config(bg='#888888'))
        date8Button.bind('<Leave>', lambda event: date8Button.config(bg='#F0F0F0'))
        date8Button.bind('<Button>', imageShow)
        date8Button.pack(anchor="ne")
        
        date9Button=Button(master=dataroot, text='1401-04-29',bg='#F0F0F0')
        date9Button.bind('<Enter>', lambda event: date9Button.config(bg='#888888'))
        date9Button.bind('<Leave>', lambda event: date9Button.config(bg='#F0F0F0'))
        date9Button.bind('<Button>', imageShow)
        date9Button.pack(anchor="nw")
        
        dataroot.mainloop()
        

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
            settingRoot.iconbitmap('icons\setting.ico')
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
    securityRoot.iconbitmap('icons\security.ico')
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

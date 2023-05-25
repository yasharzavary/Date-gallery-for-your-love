from tkinter import *
from tkinter import messagebox

# main root
root=Tk()
root.title('For My Love')
root.iconbitmap('mainroot.ico')
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

def nameAndPassControl(event):
    if nameEntry.get().upper() != 'GUMBULI':
        messagebox.showerror('Error happend', 'name isn\'t correct')
    elif passEntry.get().upper() != '1226':
        messagebox.showerror('Error happend', 'password isn\'t correct')
        

# submit button part
nameButton=Button(master=root, text='submit', bg='#F0F0F0')
nameButton.bind('<Enter>',lambda event: nameButton.config(bg='#888888'))
nameButton.bind('<Leave>',lambda event: nameButton.config(bg='#F0F0F0'))
nameButton.bind('<Button>',nameAndPassControl)
nameButton.pack()
  
def settingButton(event):
    pass

setButton=Button(master=root, text='setting', bg='#F0F0F0')
setButton.bind('<Enter>',lambda event: setButton.config(bg='#888888'))
setButton.bind('<Leave>',lambda event: setButton.config(bg='#F0F0F0'))
setButton.bind('<Button>',lambda event: root.destroy())
setButton.pack(side="bottom")

exitButton=Button(master=root, text='Exit', bg='#F0F0F0')
exitButton.bind('<Enter>',lambda event: exitButton.config(bg='#888888'))
exitButton.bind('<Leave>',lambda event: exitButton.config(bg='#F0F0F0'))
exitButton.bind('<Button>',lambda event: root.destroy())
exitButton.pack()


root.mainloop()

from tkinter import *

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
    pass

def comein(event):
    nameButton.config(bg='#888888')

def comeout(event):
    nameButton.config(bg='#F0F0F0')



# submit button part
nameButton=Button(master=root, text='submit', bg='#F0F0F0')
nameButton.bind('<Enter>',comein)
nameButton.bind('<Leave>',comeout)
nameButton.bind('<Button>',nameAndPassControl)
nameButton.pack()
    

root.mainloop()


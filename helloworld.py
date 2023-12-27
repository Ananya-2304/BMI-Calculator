from tkinter import *
root = Tk()
myLabel = Label(root,text="meow",font=("Arial Black",30))
root.geometry('350x200')
def clicked():
    myLabel.configure(text="Butto was clicked")
bt=Button(root,text="Click ME",bg="#FFFFFF",fg="red",command=clicked)
bt.place(x=50,y=30)
myLabel.pack()
bt.pack()
root.mainloop()

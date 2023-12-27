from tkinter import *
from tkinter import ttk
root=Tk()
root.title("BMI Calculator")
root.geometry("870x580+250+50")
root.resizable(False,False)
root.configure(bg="#f0f1f5")
#icon for title
icon=PhotoImage(file="assets/icon.png")
root.iconphoto(False,icon)
root.title("BMI Calculator")
#creation of frames
MainFrame=Frame(root,bd=10,width=870 ,height=580)
MainFrame.grid()
LeftFrame=Frame(MainFrame,bd=10,width=380 ,height=540 ,bg="#CCCCFF", highlightthickness=3,highlightbackground="grey",relief=RIDGE )
LeftFrame.pack(side=LEFT)
RightFrame=Frame(MainFrame,bd=10,width=490 ,height=580)
RightFrame.pack(side=RIGHT)
##########################RIGHTFRAME##############################
#################functions##############
#sliderchange height function
def sliderChangeh(event):
    formath=currentValueh.get()
    height.set(f'{formath:.2f}')
#sliderchange weight function
def sliderChangew(event):
    formatw=currentValuew.get()
    weight.set(f'{formatw:.2f}')
#BMI calculate
def calculate():
    # Retrieves all necessary information to calculate BMI
    w = float(weight.get())
    h = float(height.get())
    #to convert height from cm to m
    h=h/100
    bmi = float((w)/(h**2))
    Bmi=round(bmi,2)
    label1.configure(text=Bmi)
    if bmi < 19:
        label2.configure(text="Underweight!")
        label3.configure(text="You have a lower weight than normal")
    elif 19 <= bmi < 24:
        label2.configure(text="Normal!")
        label3.configure(text="         Wohoo! You are healthy")
    elif 25 <= bmi < 29:
        label2.configure(text="Overweight!") 
        label3.configure(text="You have higher weight than normal")
    else:
        label2.configure(text="Obese!")
        label3.configure(text="You have higher weight than normal")

###########################Styling################################
#Heading
RightFrame1=Frame(RightFrame,width=460,height=80,bg="#f5fcfa")
RightFrame1.place(x=0,y=0)
title=Label(RightFrame1,text="BMI CALCULATOR",bg="#f5fcfa",font=("Arial Black",20,),fg="black")
title.place(x=80,y=15)
#height and width boxes
box=PhotoImage(file="assets/box.png")
Label(RightFrame,image=box).place(x=10,y=100)
Label(RightFrame,image=box).place(x=230,y=100)
#Entryboxes-height
height=DoubleVar()
Label(RightFrame,text="Height in cm",bg="white",fg="grey",font="arial 15 italic").place(x=25,y=110)
heightEntry=Entry(RightFrame,textvariable=height,width=6,font="arial 40",bg="#fff",fg="#000",bd=0,justify=CENTER)
heightEntry.place(x=30,y=150)
#Entrybox-weight
weight=DoubleVar()
Label(RightFrame,text="Weight in kg",bg="white",fg="grey",font="arial 15 italic").place(x=250,y=110)
weightEntry=Entry(RightFrame,textvariable=weight,width=6,font="arial 40",bg="#fff",fg="#000",bd=0,justify=CENTER)
weightEntry.place(x=260,y=150)
#slider for height
currentValueh=DoubleVar()
style=ttk.Style()
style.configure("TScale",background="white")
slider=ttk.Scale(RightFrame,from_=0,to=200,orient=HORIZONTAL,variable=currentValueh,style="TScale",command=sliderChangeh)
slider.place(x=70,y=240)
#slider for weight
currentValuew=DoubleVar()
stylew=ttk.Style()
stylew.configure("TScale",background="white")
sliderw=ttk.Scale(RightFrame,from_=0,to=150,orient='horizontal',variable=currentValuew,style="TScale",command=sliderChangew)
sliderw.place(x=300,y=240)
#bottom box
bluebox=Label(RightFrame,width=80,height=18,bg="lightblue")
bluebox.place(x=0,y=310)
#scale
scale=PhotoImage(file="assets/scale.png")
Label(RightFrame,image=scale,bg="lightblue").place(x=10,y=312)
#childfigurescale
childImage=PhotoImage(file="assets/man.png")
Label(RightFrame,image=childImage,bg="lightblue").place(x=60,y=400)
#See BMI result button
result= Button(RightFrame, text="Submit",width=12,height=2,font="arial 10 bold",bg="#1f6e68",fg="#ffffff",command=calculate)
result.place(x=330,y=330)
label1=Label(RightFrame,font="arial 40 bold",bg="lightblue",fg="white")
label1.place(x=150,y=330)
label2=Label(RightFrame,font="arial 20 bold",bg="lightblue",fg="black")
label2.place(x=220,y=430)
label3=Label(RightFrame,font="arial 15 bold",bg="lightblue",fg="white")
label3.place(x=110,y=500)

##########################LEFT FRAME##############################
##############functions##############
def reset():
    var1.set("")
    var2.set("")
    var3.set("")
    bloodgrp.set("Select")
    height.set(0.00)
    weight.set(0.00)
    label1.configure(text="")
    label2.configure(text="")
    label3.configure(text="")


#buttons frame
Leftframe1=Frame(LeftFrame,width=350 ,height=100,bg="#CCCCFF")
Leftframe1.place(x=0,y=400)
reset=Button(Leftframe1,text="Reset",font="arial 15 bold",width=12,height=2,bg="#1f6e68",fg="#ffffff",command=reset)
reset.place(x=10,y=40)
reset=Button(Leftframe1,text="View DataTable",font="arial 15 bold",width=15,height=2,bg="#1f6e68",fg="#ffffff")
reset.place(x=160,y=40)
#variables needed for resetting
var1=StringVar()
var2=StringVar()
var3=StringVar()
#heading
label=Label(LeftFrame,text="Enter your details:",font=("times new roman",20,"bold"),bg="#CCCCFF").place(x=10,y=20)
#Name
label = Label(LeftFrame, text="Name:",font=("times new roman",15,"bold"),bg="#CCCCFF").place(x=15,y=60)
name=Entry(LeftFrame,textvariable=var1,font=(" ",15),bd=5,relief="groove")
name.place(x=20,y=100)
#Class
label = Label(LeftFrame, text="Class:",font=("times new roman",15,"bold"),bg="#CCCCFF").place(x=15,y=140) 
clas=Entry(LeftFrame, font=(" ",15),textvariable=var2,bd=5,relief="groove")
clas.place(x=20,y=180) 
#BDAY
label = Label(LeftFrame, text="Birthday:",font=("times new roman",15,"bold"),bg="#CCCCFF").place(x=15,y=220)
bday=Entry(LeftFrame,font=(" ",15),textvariable=var3,bd=5,relief="groove")
bday.place(x=20,y=260)
#Blood Group
label = Label(LeftFrame, text="Blood Group:",font=("times new roman",15,"bold"),bg="#CCCCFF").place(x=15,y=300)
bloodgrp=StringVar()
optionlist={
    'O +ve',
    'A +ve',
    'B +ve',
    'AB+ve',
    'O -ve',
    'A -ve',
    'B -ve',
    'AB-ve'
}
dropdown=OptionMenu(LeftFrame,bloodgrp,*optionlist)
dropdown.place(x=20,y=340)
bloodgrp.set("Select")

root.mainloop()
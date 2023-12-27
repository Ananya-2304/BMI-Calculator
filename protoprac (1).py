from tkinter import *

'''import mysql.connector as m
demodb=m.connect(host="localhost",user="root",passwd="alok1234",database="alok")
democursor=demodb.cursor()'''

def main():
    global height,weight,root,name,clas,bday
    root = Tk()
    root.title("BMI Calculator")
    title=Label(root,text="BMI CALACULATOR",font=("times new roman",40,"bold"),bg="yellow",fg="orange",bd=10,relief="solid")
    title.place(x=0,y=0,relwidth=1)
    #weight    
    label = Label(root, text="Enter your weight in Kg.",font=("times new roman",20,"bold")).place(y=100,x=400)  
    weight=Entry(root)
    weight.place(y=150,x=500)
    #height
    label = Label(root, text="Enter your height in meters square.",font=("times new roman",20,"bold")).place(y=200,x=400)
    height=Entry(root,font=(" ",15),bd=5,relief="groove")
    height.place(y=250,x=500)
    #Name
    label = Label(root, text="Enter your name.",font=("times new roman",20,"bold")).place(y=350,x=400)
    name=Entry(root,font=(" ",15),bd=5,relief="groove")
    name.place(y=350,x=650)
    #Class
    label = Label(root, text="Enter your class.",font=("times new roman",20,"bold")).place(y=400,x=400) 
    clas=Entry(root, font=(" ",15),bd=5,relief="groove")
    clas.place(y=400,x=650) 
    #BDAY
    label = Label(root, text="Enter your bday",font=("times new roman",20,"bold")).place(y=450,x=400)
    bday=Entry(root,font=(" ",15),bd=5,relief="groove")
    bday.place(y=450,x=650)

    # Sets a button and label to click and calculate BMI
    Button(root, text="calculate bmi", command=calculate).place(y=550,x=525)
    Button(root, text="view", command=fun2).place(y=600,x=525)
    
    root.mainloop()
        
def calculate():
    # Retrieves all necessary information to calculate BMI
    w = float(weight.get())
    h = float(height.get())
    bmi = float((w)/(h**2))
    Bmi=round(bmi,2)
                    
    if bmi < 19:
        q="You are underweight"
    if 19 <= bmi < 24:
        q="You are normal"
    if 25 <= bmi < 29:
        q="You are overweight"
    if  bmi >= 29:
        q="You are obese"

    Label(root, text="Your BMI is "+str(Bmi)+"&"+q).place(y=550,x=620)
    fun1()
        
def fun1(): 
    a=float(weight.get())
    b=float(height.get())
    g=(a)/(b**2)
    h=round(g,2)
    c=str(h)
    d=name.get()
    e=int(clas.get())
    f=bday.get()
    
    try:
        democursor.execute("Create Table If NOT exists Registration(NAME varchar(30),class int(2),bday date,BMI varchar(20))")
    finally:
        democursor.execute("INSERT INTO   Registration(NAME,class,bday,BMI) VALUES(%s, %s, %s, %s)",(d,e,f,c))
        demodb.commit()

def fun2():
    democursor.execute("select* from Registration")
    window=Tk()
    
    Label(window,text="Name",width=12).grid(row=0,column=0)
    Label(window,text="class",width=17).grid(row=0,column=1)
    Label(window,text="bday",width=9).grid(row=0,column=2)
    Label(window,text="BMI",width=9).grid(row=0,column=3)
        
    s=0
        
    for j in democursor:
        s=s+1
        q=list(j)
        
        Label(window,text=q[0]).grid(row=s,column=0)
        Label(window,text=q[1]).grid(row=s,column=1)
        Label(window,text=q[2]).grid(row=s,column=2)
        Label(window,text=q[3]).grid(row=s,column=3)
            
    window.mainloop()   
    
#start the program
main()





from tkinter import*
from math import*
from tkinter import messagebox
win=Tk()
win.geometry("300x400")
win.title("calculator")
win.resizable(0,0)
    
A=0
operator=""
val=""
operator=""
def clear():
    global A
    global operator
    global val
    val=""
    A=0
    dis_data.set(val)
def butn7():
    global val
    val=val+"7"
    dis_data.set(val)
def butn8():
    global val
    val=val+"8"
    dis_data.set(val)
def butn9():
    global val
    val=val+"9"
    dis_data.set(val)
    
def butnoop1():
    global A
    global operator
    global val
    A=int(val)
    operator="+"
    val=val+"+"
    dis_data.set(val)
        
def butn4():
    global val
    val=val+"4"
    dis_data.set(val)

def butn5():
    global val
    val+="5"
    dis_data.set(val)

def butn6():
    global val
    val+="6"
    dis_data.set(val)
def butn1():
    global val
    val+="1"
    dis_data.set(val)
def butn2():
    global val
    val+="2"
    dis_data.set(val)
def butn3():
    global val
    val+="3"
    dis_data.set(val)
def butnoop2():
    global A
    global val
    global operator
    operator="-"
    A=int(val)
    val+="-"
    dis_data.set(val)
def butnoop3():
    global A
    global operator
    global val
    operator="*"
    A=int(val)
    val+="*"
    dis_data.set(val)

def butnoop4():
    global A
    global operator
    global val
    operator="/"
    A=int(val)
    val+="/"
    dis_data.set(val)

def butn0():
    global val
    val+="0"
    dis_data.set(val)
                    
def equal():
    global val
    global A
    global operator
    val2=val
    if operator=="+":
        j=int(val2.split("+")[1])
        x=j+A
        dis_data.set(x)   
        val=str(x) 
    elif operator=="-":
        j=int(val2.split("-")[1])
        x=A-j
        dis_data.set(x)   
        val=str(x)
    elif operator=="*":
        j=int(val2.split("*")[1])
        x=j*A
        dis_data.set(x)   
        val=str(x)
    elif operator=="/":
        j=int(val2.split("/")[1])
        if j==0:
            messagebox.showerror("error","you cant divide by 0")
        else:
            x=int(A/j)
            dis_data.set(x)   
            val=str(x)
    

dis_data=StringVar()
dis=Entry(win,font=("arial",20) ,bg="purple",width=15,justify="right",bd=6,textvariable=dis_data)
dis.place(x=29,y=50)
dis.focus()

buton7=Button(win,text="7",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn7)
buton7.place(x=30,y=120)

buton8=Button(win,text="8",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn8)
buton8.place(x=90,y=120)
buton9=Button(win,text="9",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn9)
buton9.place(x=150,y=120)
butonop=Button(win,text="+",padx=5,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butnoop1)
butonop.place(x=210,y=120)

buton4=Button(win,text="4",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn4)
buton4.place(x=30,y=180)
buton5=Button(win,text="5",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn5)
buton5.place(x=90,y=180)
buton6=Button(win,text="6",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn6)
buton6.place(x=150,y=180)
butonop2=Button(win,text="-",padx=9,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butnoop2)
butonop2.place(x=210,y=180)

buton1=Button(win,text="1",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn1)
buton1.place(x=30,y=240)
buton2=Button(win,text="2",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn2)
buton2.place(x=90,y=240)
buton3=Button(win,text="3",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn3)
buton3.place(x=150,y=240)
butonop3=Button(win,text="*",padx=8,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butnoop3)
butonop3.place(x=210,y=240)

buton0=Button(win,text="0",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butn0)
buton0.place(x=30,y=300)
butonc=Button(win,text="c",padx=6,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=clear)
butonc.place(x=90,y=300)
butonop4=Button(win,text="=",padx=5,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=equal)
butonop4.place(x=150,y=300)
butonop5=Button(win,text="/",padx=9,fg="white",bg="black",font=("arial",20,"bold"),bd=6,command=butnoop4)
butonop5.place(x=210,y=300)
win.mainloop()

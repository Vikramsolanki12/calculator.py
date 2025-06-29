from tkinter import *
win=Tk()
win.geometry('400x600')
win.config(bg="grey")
win.title("Calculator")
win.resizable(False,False)


data=""
var=StringVar()
def data_get(value):
    global data
    data=data+str(value)
    var.set(data)

def clear():
    global data
    data=""
    var.set(data)

def equal():
    global data
    try:
        total=str(eval(data))
        var.set(total)
        data=""

    except:
        var.set("Error!")

frame_1=Frame(win,height=50,width=400,background="light green")
frame_1.place(x=0,y=0)
lab_1=Label(frame_1,text="CALCULATOR",font=("Times New Roman",30,"bold"),bg="light green")
lab_1.place(x=90,y=0)

ent_1=Entry(win,relief="sunken",bd=5,font=("Times New Roman",25,"bold"),textvariable=var)
ent_1.place(x=20,y=60,height=50,width=360)
#-------------------------------------------
button_clr=Button(win,text="clr",fg="red",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=clear)
button_clr.place(x=20,y=120,height=75,width=75)

button_div=Button(win,text="/",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get("/"))
button_div.place(x=115,y=120,height=75,width=75)

button_mul=Button(win,text="*",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get("*"))
button_mul.place(x=210,y=120,height=75,width=75)

button_sub=Button(win,text="-",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get("-"))
button_sub.place(x=305,y=120,height=75,width=75)
#---------------------------------------------

button_7=Button(win,text="7",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(7))
button_7.place(x=20,y=215,height=75,width=75)

button_8=Button(win,text="8",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(8))
button_8.place(x=115,y=215,height=75,width=75)

button_9=Button(win,text="9",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(9))
button_9.place(x=210,y=215,height=75,width=75)

button_add=Button(win,text="+",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get("+"))
button_add.place(x=305,y=215,height=170,width=75)
#--------------------------------------------

button_4=Button(win,text="4",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(4))
button_4.place(x=20,y=310,height=75,width=75)

button_5=Button(win,text="5",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(5))
button_5.place(x=115,y=310,height=75,width=75)

button_6=Button(win,text="6",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(6))
button_6.place(x=210,y=310,height=75,width=75)
#--------------------------------------------

button_1=Button(win,text="1",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(1))
button_1.place(x=20,y=405,height=75,width=75)

button_2=Button(win,text="2",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(2))
button_2.place(x=115,y=405,height=75,width=75)

button_3=Button(win,text="3",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(3))
button_3.place(x=210,y=405,height=75,width=75)

button_ent=Button(win,text="=",font=("Times New Roman",25,"bold"),relief="raised",bd=5,fg="green",command=equal)
button_ent.place(x=305,y=405,height=170,width=75)
#--------------------------------------------
button_zero=Button(win,text="0",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get(0))
button_zero.place(x=20,y=500,height=75,width=170)

button_dec=Button(win,text=".",font=("Times New Roman",25,"bold"),relief="raised",bd=5,command=lambda:data_get("."))
button_dec.place(x=210,y=500,height=75,width=75)








win.mainloop()
from tkinter import *  #"*" means import all function from tkinter
root = Tk()    #creat a window
root.geometry("500x600") #show a window size
root.title("Calculator")   #remae title name
l=Label(root,text="CALCULATOR",font='lucida 24 bold',bg="white",fg="black").grid(row="0",column=0,columnspan="10")  


def press(enter):
    
    global expression
    expression=expression+enter
    var.set(expression)

def total():
    try:
        global expression
        str1=eval(expression)
        
        var.set(str1)
        expression=""
    except Exception as e:
        var.set("")

    
def clear():
    global expression
    var.set("") 
    
expression=""
var=StringVar()
e=Entry(root,textvar=var,font='lucida 25 bold').grid(row=1,column=0,columnspan="8")

b1=Button(root,font='lucida 48 bold',width="2", text="C",command=clear).grid(row=2,column=0)
b2=Button(root,font='lucida 48 bold',width="2", text="%",command=lambda:press("%")).grid(row=2,column=1)
b3=Button(root,font='lucida 48 bold',width="2", text="x",command=lambda:press("x")).grid(row=2,column=2)
b4=Button(root,font='lucida 48 bold',width="2", text="/",command=lambda:press("/")).grid(row=2,column=3)
b5=Button(root,font='lucida 48 bold',width="2", text="7",command=lambda:press("7")).grid(row=3,column=0)
b6=Button(root,font='lucida 48 bold', width="2",text="8",command=lambda:press("8")).grid(row=3,column=1)
b7=Button(root,font='lucida 48 bold',width="2", text="9",command=lambda:press("9")).grid(row=3,column=2)
b8=Button(root,font='lucida 48 bold',width="2", text="*",command=lambda:press("*")).grid(row=3,column=3)
b9=Button(root,font='lucida 48 bold',width="2", text="4",command=lambda:press("4")).grid(row=4,column=0)
b10=Button(root,font='lucida 48 bold',width="2", text="5",command=lambda:press("5")).grid(row=4,column=1)
b11=Button(root,font='lucida 48 bold',width="2", text="6",command=lambda:press("6")).grid(row=4,column=2)
b12=Button(root,font='lucida 48 bold',width="2", text="-",command=lambda:press("-")).grid(row=4,column=3)
b13=Button(root,font='lucida 48 bold',width="2", text="1",command=lambda:press("1")).grid(row=5,column=0)
b14=Button(root,font='lucida 48 bold',width="2", text="2",command=lambda:press("2")).grid(row=5,column=1)
b15=Button(root,font='lucida 48 bold',width="2", text="3",command=lambda:press("3")).grid(row=5,column=2)
b16=Button(root,font='lucida 48 bold',width="2", text="+",command=lambda:press("+")).grid(row=5,column=3)
b17=Button(root,font='lucida 48 bold',width="2", text="00",command=lambda:press("00")).grid(row=6,column=0)
b18=Button(root,font='lucida 48 bold',width="2", text="0",command=lambda:press("0")).grid(row=6,column=1)
b19=Button(root,font='lucida 48 bold',width="2", text=".",command=lambda:press(".")).grid(row=6,column=2)
b20=Button(root,font='lucida 48 bold',width="2", text="=",command=total).grid(row=6,column=3)





root.mainloop()#show window
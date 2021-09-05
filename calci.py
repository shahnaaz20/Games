from tkinter import*

def btnClick(number):
    global operator
    operator=operator + str(number)
    text_Input. set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    global A
    sum=str(eval(operator))
    text_Input.set(sum)
    operator=""

cal=Tk()
cal.title("calculator")
operator=""
text_Input=StringVar()


txtDis = Entry(cal,font=('arial',20,'bold'),textvar=text_Input, bd=30,insertwidth=4,bg="powder blue",justify="right").grid(columnspan=4)


btn_clear=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="C",command= btnClearDisplay).grid(row=1,column=0)

btn_divisible=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/")).grid(row=1,column=1)

btn_bracket=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="(",command=lambda:btnClick("(")).grid(row=1,column=2)

btn_dash=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text=")",command=lambda:btnClick(")")).grid(row=1,column=3)


btn7=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9)).grid(row=2,column=2)

btn_addition=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+")).grid(row=2,column=3)


btn4=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6)).grid(row=3,column=2)

btn_subtraction=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick("-")).grid(row=3,column=3)



btn1=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3)).grid(row=4,column=2)

btn_multipication=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*")).grid(row=4,column=3)


btn_module=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="%",command=lambda:btnClick("%")).grid(row=5,column=0)

btn_zero=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick("0")).grid(row=5,column=1)

btn_dot=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text=".",command=lambda:btnClick(".")).grid(row=5,column=2)

btn_equal=Button(cal,padx=16, bd=8,fg="black",font=('arial',20,'bold'),text="=",command=btnEqualsInput).grid(row=5,column=3)

cal.mainloop()
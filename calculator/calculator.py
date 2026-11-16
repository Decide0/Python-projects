from tkinter import *
from tkinter import messagebox
num1 = 0
num2 = 0
sign = ''

def fun1():
    if int(label.cget('text')) == 0:
        new_text = '1'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '1'
        label.config(text= new_text)
def fun2():
    if int(label.cget('text')) == 0:
        new_text = '2'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '2'
        label.config(text= new_text)
def fun3():
    if int(label.cget('text')) == 0:
        new_text = '3'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '3'
        label.config(text= new_text)
def fun4():
    if int(label.cget('text')) == 0:
        new_text = '4'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '4'
        label.config(text= new_text)
def fun5():
    if int(label.cget('text')) == 0:
        new_text = '5'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '5'
        label.config(text= new_text)

def fun6():
    if int(label.cget('text')) == 0:
        new_text = '6'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '6'
        label.config(text= new_text)

def fun7():
    if int(label.cget('text')) == 0:
        new_text = '7'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '7'
        label.config(text= new_text)
def fun8():
    if int(label.cget('text')) == 0:
        new_text = '8'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '8'
        label.config(text= new_text)
def fun9():
    if int(label.cget('text')) == 0:
        new_text = '9'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '9'
        label.config(text= new_text)
def fun0():
    if int(label.cget('text')) == 0:
        new_text = '0'
        label.config(text= new_text)
    else:
        new_text = label.cget('text') + '0'
        label.config(text= new_text)

def funP():
    global num1, sign
    num1 = int(label.cget('text'))
    label.config(text='0')
    sign = '+'

def funM():
    global num1, sign
    sign = '-'
    num1 = int(label.cget('text'))
    label.config(text='0')
def funMt():
    global num1,sign
    sign = '*'
    num1 = int(label.cget('text'))
    label.config(text='0')
def funD():
    global num1,sign
    sign = '/'
    num1 = int(label.cget('text'))
    label.config(text='0')

def funE():
    global num1, num2, sign
    num2 = int(label.cget('text'))
    result = 0
    if sign == '+':
        result = num1 + num2
    elif sign == '-':
        result = num1 - num2
    elif sign == '*':
        result = num1 * num2
    elif sign == '/':
        if num2 !=0:
            result = num1 / num2
        else:
            messagebox.showerror(title='Division Error', message='You can not divide by ZERO')
    label.config(text=f'{result}')

def funC():
    label.config(text='0')

window = Tk()
window.title('Calculator')
window.config(padx=10,pady=10, bg='Indigo')
window.minsize(width=200,height=200)

label = Label(text='0' ,width=20, padx=10,pady=15, bg='Indigo', fg='White',anchor='e')
label.grid(row=0,column=1,columnspan=3)

btn1 = Button(text='1', width=5, command=fun1, highlightbackground='MediumPurple')
btn1.grid(row=1,column=0, pady = 5)

btn2 = Button(text='2', width=5, command=fun2, highlightbackground='MediumPurple')
btn2.grid(row=1,column=1)

btn3 = Button(text='3', width=5, command=fun3, highlightbackground='MediumPurple')
btn3.grid(row=1,column=2)

btn4 = Button(text='4', width=5, command=fun4, highlightbackground='MediumPurple')
btn4.grid(row=2,column=0, pady = 5)

btn5 = Button(text='5', width=5, command=fun5, highlightbackground='MediumPurple')
btn5.grid(row=2,column=1)

btn6 = Button(text='6', width=5, command=fun6, highlightbackground='MediumPurple')
btn6.grid(row=2,column=2)

btn7 = Button(text='7', width=5, command=fun7, highlightbackground='MediumPurple')
btn7.grid(row=3,column=0, pady = 5)

btn8 = Button(text='8', width=5, command=fun8, highlightbackground='MediumPurple')
btn8.grid(row=3,column=1)

btn9 = Button(text='9', width=5, command=fun9, highlightbackground='MediumPurple')
btn9.grid(row=3,column=2)

btn0 = Button(text='0', width=14, command=fun0, highlightbackground='MediumPurple')
btn0.grid(row=4,column=0, columnspan=2)



#side buttons
btnP = Button(text='+', command=funP, highlightbackground='MediumPurple', width = 2)
btnP.grid(row=1,column=3)

btnM = Button(text='-', command=funM, highlightbackground='MediumPurple', width = 2)
btnM.grid(row=2,column=3)

btnMt = Button(text='*', command=funMt, highlightbackground='MediumPurple', width = 2)
btnMt.grid(row=3,column=3)

btnD = Button(text='/', command=funD, highlightbackground='MediumPurple', width = 2)
btnD.grid(row=4,column=3)

btnE = Button(text='=', width=5, command=funE, highlightbackground='MediumPurple')
btnE.grid(row=4,column=2)


btnC = Button(text='C', width=5, command=funC, highlightbackground='MediumPurple')
btnC.grid(row=0,column=0)
window.mainloop()
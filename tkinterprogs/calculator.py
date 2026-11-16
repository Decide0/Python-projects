import tkinter

window = tkinter.Tk()
window.title('Calculator')
window.minsize(height = 100, width = 200)
window["bg"] = "Indigo"

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

label = tkinter.Label(text = '0', background = 'Indigo', foreground = 'White')
label.grid(row = 0 , column  = 1, columnspan = 2)

#Digits

button1 = tkinter.Button(text = '1', width = 10, command = fun1)
button1.grid(row = 1, column  = 0, pady = 5)

button2 = tkinter.Button(text = '2', width = 10, command = fun2)
button2.grid(row = 1, column  = 1)

button3 = tkinter.Button(text = '3', width = 10, command = fun3)
button3.grid(row = 1, column  = 2)

button4 = tkinter.Button(text = '4', width = 10, command = fun4)
button4.grid(row = 2, column  = 0)

button5 = tkinter.Button(text = '5', width = 10, command = fun5)
button5.grid(row = 2, column  = 1)

button6 = tkinter.Button(text = '6', width = 10, command = fun6)
button6.grid(row = 2, column  = 2)

button7 = tkinter.Button(text = '7', width = 10, command = fun7)
button7.grid(row = 3, column  = 0)

button8 = tkinter.Button(text = '8', width = 10, command = fun8)
button8.grid(row = 3, column  = 1)

button9 = tkinter.Button(text = '9', width = 10, command = fun9)
button9.grid(row = 3, column  = 2)

button0 = tkinter.Button(text = '0', width = 22)
button0.grid(row = 4, column  = 0, columnspan = 2)


#Operations

button_c = tkinter.Button(text = 'C', width = 10)
button_c.grid(row = 0, column = 0)

button_plus = tkinter.Button(text = '+', width = 1)
button_plus.grid(row = 1, column  = 3)

button_mines = tkinter.Button(text = '-', width = 1)
button_mines.grid(row = 2, column  = 3)

button_mul = tkinter.Button(text = '*', width = 1)
button_mul.grid(row = 3, column  = 3)

button_mul = tkinter.Button(text = '/', width = 1)
button_mul.grid(row = 4, column  = 3)

button_eq = tkinter.Button(text = '=', width = 10)
button_eq.grid(row = 4, column  = 2)













window.mainloop()
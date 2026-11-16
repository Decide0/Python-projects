import tkinter

window = tkinter.Tk()

def formula():
    a = int(my_entry.get())
    b = a * 1.609
    label4.config(text = b)


window.title('My TK Program')
window.minsize(height = 200, width = 200)

label = tkinter.Label(text = 'Miles')
label.grid(row = 0, column = 2)

my_entry = tkinter.Entry()
my_entry.grid(row = 0, column = 1)

label2 = tkinter.Label(text = 'is equal to')
label2.grid(row = 1, column = 0)

label3 = tkinter.Label(text = 'Km')
label3.grid(row = 1, column = 2)

label4 = tkinter.Label(text = '0')
label4.grid(row = 1, column = 1)

mybutton = tkinter.Button(text = 'Calculate', command = formula)
mybutton.grid(row = 2, column = 1)


window.mainloop()
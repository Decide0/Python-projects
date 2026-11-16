import random
from tkinter import *
from string import *

def passg():
    new_pass = ''
    password = ''
    password += ascii_lowercase + ascii_uppercase + punctuation + digits
    password = random.sample(password, k = 10)
    for i in password:
        new_pass += i
    password_e.delete(0, END)
    password_e.insert(0, new_pass)

def save():
    with open('./data.txt', mode = 'a') as data:
        web = website_e.get()
        name = user_e.get()
        pass_w = password_e.get()
        data.write(f'\nWebsite: {web}\nUser Name: {name}\nPassword: {pass_w}')



window = Tk()
window.title('Data Saver')
window.minsize(height = 400, width = 400)
window.config(bg = 'Black', pady = 5, padx = 5)

canvas = Canvas(width = 1200, height = 500, bg = 'Black', highlightthickness = 0)
img = PhotoImage(file = './tkinterprogs/image.png')
canvas.create_image(600, 315, image = img)
canvas.grid(row = 0, column = 0, columnspan = 3)

website_l = Label(text = 'Website:', fg = 'White', bg = 'Black', font = 16)
website_l.grid(row = 1, column = 0)

website_e = Entry(width = 100)
website_e.grid(row = 1, column = 1, pady= 10)

user_l = Label(text = 'Email/Username:', fg = 'White', bg = 'Black', font = 16)
user_l.grid(row = 2, column = 0)

user_e = Entry(width = 100)
user_e.grid(row = 2, column = 1, pady= 10)

password = Label(text = 'Password:', fg = 'White', bg = 'Black', font = 16)
password.grid(row = 3, column = 0)

password_e = Entry(width = 100)
password_e.grid(row = 3, column = 1, pady= 10)

gen_pass = Button(text = 'Generate Password', width = 30, command = passg)
gen_pass.grid(row = 3, column = 2)

save = Button(text = 'Add', width = 30, command = save)
save.grid(row = 4, column = 0, columnspan= 2)

window.mainloop()

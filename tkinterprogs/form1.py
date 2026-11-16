import tkinter

def save1():
    with open('./student_data.txt', mode = 'a') as data:
        name = entry.get()
        surname = entry2.get()
        phone_num = entry3.get()
        Address = entry4.get()
        data.write(f'{name},{surname},{phone_num},{Address}\n')
    
    entry.insert(0, string='')
    entry2.insert(0, string = '')
    entry3.insert(0, string = '')
    entry4.insert(0, string = '')
        
    
window = tkinter.Tk()
window.title('Data Saver')
window.minsize(height = 80, width= 200)

#Labels
label_name = tkinter.Label(text = 'Name :', anchor = 'w', width = 15)
label_name.grid(row = 0, column = 0)

label_surname = tkinter.Label(text = 'Surename :', anchor = 'w', width = 15)
label_surname.grid(row = 1, column = 0)

label_phone = tkinter.Label(text = 'Phone number :', anchor = 'w', width = 15)
label_phone.grid(row = 2, column = 0)

label_address = tkinter.Label(text = 'Address : ', anchor = 'w', width = 15)
label_address.grid(row = 3, column = 0)

#USER

entry = tkinter.Entry()
entry.grid(row = 0, column = 1)

entry2 = tkinter.Entry()
entry2.grid(row = 1, column = 1)

entry3 = tkinter.Entry()
entry3.grid(row = 2, column = 1)

entry4 = tkinter.Entry()
entry4.grid(row = 3, column = 1)

#Button

save = tkinter.Button(text = 'Save', width = 10, command = save1)
save.grid(row = 4, column = 0, columnspan = 2, pady = 5)










window.mainloop()
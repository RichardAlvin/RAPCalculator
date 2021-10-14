from tkinter import *

root = Tk()
root.title("Simple Calculator")
#root.geometry("300x500")

#navbar Tab Frames
def simple_calc():
    global e
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

    #Put the buttons on the screen
    button_1.grid(row=3 ,column=0)
    button_2.grid(row=3 ,column=1)
    button_3.grid(row=3 ,column=2)

    button_4.grid(row=2 ,column=0)
    button_5.grid(row=2 ,column=1)
    button_6.grid(row=2 ,column=2)

    button_7.grid(row=1 ,column=0)
    button_8.grid(row=1 ,column=1)
    button_9.grid(row=1 ,column=2)

    button_0.grid(row=4 ,column=0)

    button_clear.grid(row=4, column=1,columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_substract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)
    #simple_calc_frame.pack(fill="both", expand=1)

def scientific_calc():
    global e
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

    #Put the buttons on the screen
    button_1.grid(row=3 ,column=0)
    button_2.grid(row=3 ,column=1)
    button_3.grid(row=3 ,column=2)

    button_4.grid(row=2 ,column=0)
    button_5.grid(row=2 ,column=1)
    button_6.grid(row=2 ,column=2)

    button_7.grid(row=1 ,column=0)
    button_8.grid(row=1 ,column=1)
    button_9.grid(row=1 ,column=2)

    button_0.grid(row=5 ,column=0)
    

def programmer_calc():
    return

def history():
    return



#Navbar Tab
menubar = Menu(root)
dropMenu_1 = Menu(menubar, tearoff=0)
dropMenu_1.add_command(label="Simple", command=simple_calc)
dropMenu_1.add_command(label="Scientific", command=scientific_calc)
dropMenu_1.add_command(label="Programmer", command=programmer_calc)
menubar.add_cascade(label="View", menu=dropMenu_1)

menubar.add_command(label="History", command=history)
menubar.add_command(label="Shutdown", command=root.quit)

root.config(menu=menubar)





#e.insert(0, "Enter Your Name: ")

def button_add():
    return

def button_clear():
    e.delete(0, END)

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addittion"
    f_num = int(first_number)
    e.delete(0, END)

def button_substract():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "substraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))


# #define the button
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=89, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_substract = Button(root, text="-", padx=41, pady=20, command=button_substract)
button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)



#create a frame
simple_calc_frame = Frame(root, width=400, height=400, bg="red")

root.mainloop()
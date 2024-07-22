from tkinter import*
cal = Tk()
cal.title("Simple calculator")
frame =Frame(master=cal, bg="skyblue", padx=10)
frame.pack()
e=Entry(master=frame, width=35, borderwidth=15)
e.grid(row=0, column=0, columnspan=20, padx=10, pady=20)
def  button_click(number):
    current=e.get()#creating new variable for inserting a number in correct order
    e.delete(0,END)#used for delete the previously used numbers
    e.insert(0,str(current) + str(number))#str function make sure that it is absolutely string 
def button_clear():
    e.delete(0,END)
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num + int(second_number)) 
    if math == "subtraction":
        e.insert(0,f_num - int(second_number)) 
    if math == "multiplication":
        e.insert(0,f_num * int(second_number)) 
    if math == "division":
        e.insert(0,f_num / int(second_number)) 


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)    
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)
#creating a buttons
button1 = Button(master=frame, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(master=frame, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(master=frame, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(master=frame, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(master=frame, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(master=frame, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(master=frame, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(master=frame, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(master=frame, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(master=frame, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(master=frame, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(master=frame, text="=", padx=39, pady=20, command=button_equal)
button_clear = Button(master=frame, text="clear", padx=31, pady=20, command=button_clear)
button_subtract = Button(master=frame, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(master=frame, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(master=frame, text="/", padx=40, pady=20, command=button_divide)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=1)

button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
cal.mainloop()

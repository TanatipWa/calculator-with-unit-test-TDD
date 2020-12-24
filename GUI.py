import tkinter
from tkinter import *
from tkinter import messagebox

import calculater as cal

val = ""
A = 0
operator = ""
clickPoint = False
#---------------------------------------------------------------------------------------------
def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)
def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)
def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)
def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)
def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)
def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)
def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)
def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)
def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)
def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)
def btn_point_isclicked():
    global val
    global clickPoint
    if(clickPoint == False):
        val = val + "."
        clickPoint = True
        data.set(val)
#---------------------------------------------------------------------------------------------
def btn_plus_isclicked():
    global A
    global operator
    global val
    global clickPoint
    if (clickPoint == False): A = int(val)
    elif (clickPoint == True): A = float(val)
    operator = "+"
    val = val + "+"
    clickPoint = False
    data.set(val)
def btn_min_isclicked():
    global A
    global operator
    global val
    global clickPoint
    if (clickPoint == False): A = int(val)
    elif (clickPoint == True): A = float(val)
    operator = "-"
    val = val + "-"
    clickPoint = False
    data.set(val)
def btn_mult_isclicked():
    global A
    global operator
    global val
    global clickPoint
    if (clickPoint == False): A = int(val)
    elif (clickPoint == True): A = float(val)
    operator = "*"
    val = val + "*"
    clickPoint = False
    data.set(val)
def btn_div_isclicked():
    global A
    global operator
    global val
    global clickPoint
    if (clickPoint == False): A = int(val)
    elif (clickPoint == True): A = float(val)
    operator = "/"
    val = val + "/"
    clickPoint = False
    data.set(val)
def btn_c_isclicked():
    global A
    global operator
    global val
    global clickPoint
    val = ""
    A = 0
    operator = ""
    clickPoint = False
    data.set(val)

def result():
    global A
    global operator
    global val
    global clickPoint
    val2 = val
    if operator == "+":
        if (clickPoint == False): x = int((val2.split("+")[1]))
        elif (clickPoint == True): x = float((val2.split("+")[1]))
        C = cal.add(A, x) #CALL CALCULATOR FUNCTION
        data.set(C)
        val = str(C)
    elif operator == "-":
        if (clickPoint == False): x = int((val2.split("-")[1]))
        elif (clickPoint == True): x = float((val2.split("-")[1]))
        C = cal.minus(A, x) #CALL CALCULATOR FUNCTION
        data.set(C)
        val = str(C)
    elif operator == "*":
        if (clickPoint == False): x = int((val2.split("*")[1]))
        elif (clickPoint == True): x = float((val2.split("*")[1]))
        C = cal.multipy(A, x) #CALL CALCULATOR FUNCTION
        data.set(C)
        val = str(C)
    elif operator == "/":
        if (clickPoint == False): x = int((val2.split("/")[1]))
        elif (clickPoint == True): x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By Zero Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = cal.divi(A, x) #CALL CALCULATOR FUNCTION
            data.set(C)
            val = str(C)
    clickPoint = False

#---------------------------------------------------------------------------------------------
root = tkinter.Tk()
root.geometry("400x550+300+300")
root.resizable(0, 0)
root.title("Calculator")

data = StringVar()
lbl = Label(root, text="Label", anchor=SE, font = ("Verdana", 20), textvariable = data, background = "#ffffff", fg = "#000000")
lbl.pack(expand= True, fill = "both")

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both",)
btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both",)
btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both",)
btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both",)
btnrow5 = Frame(root)
btnrow5.pack(expand=True, fill="both",)

btn7 = Button(btnrow1, text = "7", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_7_isclicked,)
btn7.pack(side=LEFT, expand=True, fill="both",)
btn8 = Button(btnrow1, text = "8", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_8_isclicked,)
btn8.pack(side=LEFT, expand=True, fill="both",)
btn9 = Button(btnrow1, text = "9", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_9_isclicked,)
btn9.pack(side=LEFT, expand=True, fill="both",)
btn_plus = Button(btnrow1, text = "+", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_plus_isclicked,)
btn_plus.pack(side=LEFT, expand=True, fill="both",)

btn4 = Button(btnrow2, text = "4", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_4_isclicked,)
btn4.pack(side=LEFT, expand=True, fill="both",)
btn5 = Button(btnrow2, text = "5", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_5_isclicked,)
btn5.pack(side=LEFT, expand=True, fill="both",)
btn6 = Button(btnrow2, text = "6", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_6_isclicked,)
btn6.pack(side=LEFT, expand=True, fill="both",)
btn_min = Button(btnrow2, text = "-", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_min_isclicked,)
btn_min.pack(side=LEFT, expand=True, fill="both",)

btn1 = Button(btnrow3, text = "1", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_1_isclicked,)
btn1.pack(side=LEFT, expand=True, fill="both",)
btn2 = Button(btnrow3, text = "2", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_2_isclicked,)
btn2.pack(side=LEFT, expand=True, fill="both",)
btn3 = Button(btnrow3, text = "3", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_3_isclicked,)
btn3.pack(side=LEFT, expand=True, fill="both",)
btn_mult = Button(btnrow3, text = "*", font = ("Verdana", 22), relief = GROOVE, border = 0,command = btn_mult_isclicked,)
btn_mult.pack(side=LEFT, expand=True, fill="both",)

btnC = Button(btnrow4, text = "C", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_c_isclicked,)
btnC.pack(side=LEFT, expand=True, fill="both",)
btn0 = Button(btnrow4, text = "0", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_0_isclicked,)
btn0.pack(side=LEFT, expand=True, fill="both",)
btn_point = Button(btnrow4, text = ".", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_point_isclicked,)
btn_point.pack(side=LEFT, expand=True, fill="both",)
btn_div = Button(btnrow4, text = "/", font = ("Verdana", 22), relief = GROOVE, border = 0, command = btn_div_isclicked)
btn_div.pack(side=LEFT, expand=True, fill="both",)

btn_equal = Button(btnrow5, bg="#50B0CF", text = "=", font = ("Verdana", 22), relief = GROOVE, border = 0, command = result)
btn_equal.pack(side=LEFT, expand=True, fill="both",)

root.mainloop()


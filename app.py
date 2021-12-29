import tkinter as tk
import math
from tkinter.constants import END

################################################
############## THE FUNCTIONALITY ###############
################################################

# CALCULATION FUNCTIONS

def add(a,b):
    print(a + b)
    return a + b

def sub(a,b):
    print(a - b)
    return a - b

def mult(a,b):
    print(a * b)
    return a * b

def div(a,b):
    print(a/b)
    return a/b

def sqr(a):
    print(a * a)
    return a * a

def sqrRt(a):
    print(math.sqrt(a))
    return math.sqrt(a)

def exp(a,b):
    print (a**b)
    return a ** b

# GIVING THE BUTTONS EVENT LISTENERS

numstr1=''
operstr=''
numstr2=''
numsArr=["7", "8", "9", "0", "4", "5", "6", "1", "2", "3", "."]
operArr=["sqr()", "√", "+", "-", "x", "/", "exp", "C", "="]

btnsDict={"sqr()": sqr, "√": sqrRt, "+": add, "-": sub, "x": mult, "/": div, "exp": exp}

def clear():
    global numstr1
    global numstr2
    global operstr

    numstr1=''
    numstr2=''
    operstr=''
    entry.delete(0, tk.END)

def btnClick(btntext):
    global numstr1
    global numstr2
    global operstr

    if btntext in numsArr:
        if operstr == "":
            numstr1 += btntext
            entry.insert(tk.END, btntext)
        else:
            numstr2 += btntext
            entry.insert(tk.END, btntext)
    elif btntext in operArr and numstr1 != "" and btntext != "C":
        if operstr == "":
            operstr = btntext
            entry.insert(tk.END, btntext)
        else:
            if "." in numstr1 or "." in numstr2:
                num1 = float(numstr1)
                if operstr != "sqr()" and operstr != "√":
                    print("my operator is not sqr() or √")
                    num2 = float(numstr2)
                print("the number had a decimal in it")
            else:
                num1 = int(numstr1)
                if operstr != "sqr()" and operstr != "√":
                    print("my operator is not sqr() or √")
                    num2 = int(numstr2)
                print("the number was an integer")
            entry.delete(0, tk.END)
            if operstr != "sqr()" and operstr != "√":
                entry.insert(0, btnsDict[operstr](num1, num2))
            else:
                entry.insert(0, btnsDict[operstr](num1))
            numstr1 = entry.get()
            if btntext != "=":
                operstr = btntext
                entry.insert(tk.END, btntext)
            else:
                operstr = ""
            numstr2 = ""

    elif btntext == "C":
        clear()
    elif btntext in operArr and numstr1 == "" and btntext != "C":
        print("INVALID INPUT /n Please click a number first")
        entry.delete(0, tk.END)
        entry.insert(0, "INVALID INPUT")

    print ("button text = " + btntext)
    print ("operator = " + operstr)
    print ("numstr1 = " + numstr1)
    print ("numstr2 = " + numstr2)
    


#####################################
############## THE UI ###############
#####################################

# CREATING THE WINDOW

window = tk.Tk() # <-- the Tk() class causes a window to open; we've assigned this window to the variable "window"
window.title("Python Tkinter Calculator")

window.configure(background="gray") # <-- makes the background of the window gray; you can also use hexadecimals
window.geometry("600x600")

# CREATING THE CALCULATOR BACKGROUND

canvas = tk.Canvas(window, background="purple", width=400, height=500) # <-- canvas is our window frame/ the inside part of our window
canvas.grid(columnspan=4, rowspan=6) # we create a number of grid rows and columns that are invisible

"""
        C O L U M N S
    0.0  0.1  0.2  0.3   
R   1.0  1.1  1.2  1.3  
O   2.0  2.1  2.2  2.3   
W   3.0  3.1  3.2  3.3  
S   4.0  4.1  4.2  4.3   
    5.0  5.1  5.2  5.3 
"""

# CREATING THE ENTRY/USER INPUT BOX

entry = tk.Entry(window) # <-- dont try to do .grid or .place on the same line that you declared the tk.Entry() on -- it will throw an error
entry.grid(row=0, column=0, columnspan=3)
entry.place(width=389, height=50, x=7, y=3)
#entry.pack(side=tk.LEFT, padx=3) <-- cant do pack while youre also using grid

# CREATING CALCULATOR BUTTONS

BtnsArr = ["clrBtn", "sqrBtn", "sqrRtBtn", "plusBtn", "SvnBtn", "EigBtn", "NineBtn", "minusBtn", "FourBtn", "FiveBtn", "SixBtn", "mulBtn", "oneBtn", "TwoBtn", "ThreeBtn", "divBtn", "decBtn", "zeroBtn", "expBtn", "equalBtn"]
BtnsTextArr = ["C", "sqr()", "√", "+", "7", "8", "9", "-", "4", "5", "6", "x", "1", "2", "3", "/", ".", "0", "exp", "="]

r = 1
indx1 = 0
indx2 = 0
while indx1 <= 4:
    for x in range(4):
        c = x
        print(BtnsArr[indx2] + "button is being created with text: " + BtnsTextArr[indx2] )
        BtnsArr[indx2] = tk.Button(window, text=BtnsTextArr[indx2], width=11, height=3, command=lambda btntext=BtnsTextArr[indx2]: btnClick(btntext)) .grid(row=r, column=c) # if you're going to use a loop to create buttons, you need to have a lambda command and if your command function is going to have parameters, you will need to define the values of the parameter (btntext = BtnTextArr[indx2]) in each loop otherwise the values will all be the same for each loop
        indx2 += 1
    r+=1
    indx1 += 1

# RUN THE WINDOW

window.mainloop() # <-- tells the program to run/open the window

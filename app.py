import tkinter as tk
import math
from tkinter.constants import END


################################################
############## THE FUNCTIONALITY ###############
################################################

# GIVING THE BUTTONS EVENT LISTENERS

numstr1=''
operstr=''
numstr2=''
numsArr=["7", "8", "9", "0", "4", "5", "6", "1", "2", "3"]
operArr=["sqr()", "√", "+", "-", "x", "/", ".", "exp"]

btnsDict={"sqr()": "sqr", "√": "sqrRt", "+": "add", "-": "sub", "x": "mult", "/": "div", "exp": "exp"}

"""
DELETE LATER

def num1():
    global numstr1
    numstr1 = numstr1 + entry.get()

def operBtns():
    global operstr
    operstr = entry.get()

def num2():
    global numstr2
    numstr2 = numstr2 + entry.get()
"""

def clear():
    global numstr1
    global numstr2
    #global operstr

    numstr1=''
    numstr2=''
    #operstr=''
    entry.delete(0, END)

def btnClick(btntext):
    global numstr1
    global numstr2
    global operstr
    print (btntext)
    print (btntext)
    if btntext in numsArr:
        if operstr == "":
            numstr1 += btntext
        else:
            numstr2 += btntext
    elif btntext in operArr and numstr1 != "":
        if operstr == "":
            operstr = btntext
        else:
            if "." in numstr1 or "." in numstr2:
                num1 = float(numstr1)
                num2 = float(numstr2)
            else:
                num1 = int(numstr1)
                num2 = int(numstr2)
            entry.insert(0, dict.get(operstr(num1, num2)))
    elif btntext in operArr and numstr1 == "":
        entry.insert(0, "INVALID INPUT")
    
    clear()

# CALCULATE

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
    c = a
    for x in range(b-1):
        c = c * a
    print(c)
    return c

# BUTTON FUNCTIONS

"""
CALCULATOR BUTTONS TESTING

BtnsArr = ["clrBtn", "sqrBtn", "sqrRtBtn", "plusBtn", "SvnBtn", "EigBtn", "NineBtn", "minusBtn", "FourBtn", "FiveBtn", "SixBtn", "mulBtn", "oneBtn", "TwoBtn", "ThreeBtn", "divBtn", "decBtn", "zeroBtn", "expBtn", "equalBtn"]
BtnsTextArr = ["C", "sqr()", "√", "+", "7", "8", "9", "-", "4", "5", "6", "x", "1", "2", "3", "/", ".", "0", "exp", "="]

r = 0
num1 = 0
num2 = 0
while num1 <= 4:
    for x in range(4):
        c = x
        print(BtnsArr[num2] + " " + BtnsTextArr[num2] + " " + "row="+ str(r) + " " + "column=" + str(c))
        num2 += 1
    r+=1
    num1 += 1
"""




"""
Placing an Image in the GUI:

photo = PhotoImage(file="photo.gif") # <-- creates a variable called photo that has the value of your local image file
Label (window, image=photo, bg="green") .grid(row=0, column= 2, sticky=W) # <-- a label for the image file that is in charge of telling 
                                                                                    what window the image will be in, 
                                                                                    what the backgorund color of the  image will be, 
                                                                                    the row and column det the image will be in
                                                                                    whether the image will stay in he N, W, E, or S of the window when it is shrunken and enlarged
"""

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
# change to a dictionary

r = 1
num1 = 0
num2 = 0
while num1 <= 4:
    for x in range(4):
        c = x
        BtnsArr[num2] = tk.Button(window, text=BtnsTextArr[num2], width=11, height=3, command=btnClick(BtnsTextArr[num2])) .grid(row=r, column=c)
        num2 += 1
    r+=1
    num1 += 1


# RESULTS

results = "RESULTS: "
resultsText = tk.Label(window, text=results, width=10, height=2) .grid(row=6, column=0, columnspan=3)


window.mainloop() # <-- tells the program to run/open the window

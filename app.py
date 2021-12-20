import tkinter as tk

window = tk.Tk() # <-- the Tk() class causes a window to open; we've assigned this window to the variable "window"
window.title("Python Tkinter Calculator")

window.configure(background="black") # <-- makes the background of the window black; you can also use hexadecimals
window.geometry("600x600")

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

# INPUT BOX
entry = tk.Entry(window) .grid(row=0, column=0, columnspan=3)


# CALCULATOR BUTTONS

BtnsArr = ["clrBtn", "sqrBtn", "sqrRtBtn", "plusBtn", "SvnBtn", "EigBtn", "NineBtn", "minusBtn", "FourBtn", "FiveBtn", "SixBtn", "mulBtn", "oneBtn", "TwoBtn", "ThreeBtn", "divBtn", "decBtn", "zeroBtn", "expBtn", "equalBtn"]
BtnsTextArr = ["C", "sqr()", "√", "+", "7", "8", "9", "-", "4", "5", "6", "x", "1", "2", "3", "/", ".", "0", "exp", "="]

r = 1
num1 = 0
num2 = 0
while num1 <= 4:
    for x in range(4):
        c = x
        BtnsArr[num2] = tk.Button(window, text=BtnsTextArr[num2], width=11, height=3) .grid(row=r, column=c)
        num2 += 1
    r+=1
    num1 += 1





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

window.mainloop() # <-- tells the program to run/open the window

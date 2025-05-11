from random import randint, choice
from tkinter import *
import pyperclip

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
signs = ['+', '=', '(', ')', '*', '&', '?', '^', '$', '#', '@', '-', '!', '~', '`', ':', ';', '/', ',', '.', '{', '}', '>', '<', '|', '[', ']', '%', '"', "'"]

def generate():

    out = ''
    seq = []
    
    up = isUpper.get()
    low = isLower.get()
    nums = isNum.get()
    sign = isSigns.get()
    
    if length.get() == '':
        output('Error: need to select password length', 'red')
        return 0

    ln = int(length.get())
    
    a = up + low + nums + sign
    if a == 0: 
        output('Error: need to select some settings options', 'red')
        return 0
        
    if up: seq.append('up')
    if low: seq.append('low')
    if nums: seq.append('nums')
    if sign: seq.append('sign')
    
    for i1 in range(ln):
        b = choice(seq)
        if b == 'up': out += upper[randint(0, 25)]
        elif b == 'low': out += lower[randint(0, 25)]
        elif b == 'nums': out += num[randint(0, 9)]
        else: out += signs[randint(0, 29)]
                
    output(out, 'black')
    
def output(out, color):
    out_entry = Entry(gen, foreground = color, width = 50)
    out_entry.insert(0, out)
    out_entry.grid(row = 2, column = 4)
    pyperclip.copy(out)

gen = Tk()
gen.geometry('560x140')
gen.title('Password generator')
gen.resizable(width = False, height = False)

isUpper = BooleanVar()
isLower = BooleanVar()
isNum = BooleanVar()
isSigns = BooleanVar()
length = StringVar()

settings_text = Label(gen, text = 'Settings:')
settings_text.grid(row = 0, column = 0)

len_pass = Label(gen, text = 'Length of password:')
len_pass.grid(row = 4, column = 0)

len_pass_input = Entry(gen, textvariable = length)
len_pass_input.grid(row = 4, column = 1)

flag1 = Checkbutton(gen, text = 'Upper symbols', variable = isUpper, onvalue = True, offvalue = False)
flag1.grid(row = 0, column = 1)

flag2 = Checkbutton(gen, text = 'Lower symbols', variable = isLower, onvalue = True, offvalue = False)
flag2.grid(row = 1, column = 1)

flag3 = Checkbutton(gen, text = 'Number symbols', variable = isNum, onvalue = True, offvalue = False)
flag3.grid(row = 2, column = 1)

flag4 = Checkbutton(gen, text = 'Special symbols', variable = isSigns, onvalue = True, offvalue = False)
flag4.grid(row = 3, column = 1)

gen_button = Button(gen, text = 'Generate', command = generate)
gen_button.grid(row = 1, column = 4)

gen.mainloop()
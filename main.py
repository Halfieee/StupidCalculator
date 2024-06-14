import tkinter as tk
from tkinter import ttk

value1 = ""
value2 = ""
znak = ""
znakpressed = False
wynik = 0
equalpressed = False

class Buttons:
    def __init__(self, master, text, command):
        self.command = command
        self.master = master
        self.text = text

    def place(self, x, y):
        self.place = tk.Button(self.master,borderwidth=1, relief='groove', font=("Helvetica", 14), text=self.text, command=self.command, height=2, width=2).place(x=x, y=y)

class Outputs:
    def __init__(self, textvar, x, y):
        self.label = tk.Label(font=('Terminal', 30), text=textvar, bg='#33FF00')
        self.label.place_forget()
        self.label.place(x=x, y=y)

class Canvas:
    def __init__(self, master, width, height,bg, borderwidth, relief):
        self.master = master
        self.width = width
        self.height = height
        self.bg = bg
        self.relief = relief
        self.borderwidth = borderwidth
    def place(self, x, y):
        self.place = tk.Canvas(self.master, width=self.width, height=self.height, bg=self.bg, borderwidth=self.borderwidth, relief=self.relief, highlightthickness=0).place(x=x, y=y)

    #w/o border alt place
    def placenoborder(self, x, y):
        self.place = tk.Canvas(self.master, width=self.width, height=self.height, bg=self.bg, highlightthickness=0).place(x=x, y=y)

def main():
    #root
    root = tk.Tk()
    root.geometry('320x400')
    root.title('Kalkulator na infe')
    root.resizable(False, False)

    #Szary kolor tla
    mainbg = Canvas(root, 325, 455, '#787976', False, False)
    mainbg.placenoborder(-1, -1)

    #zielony output
    outbg = Canvas(root, 280, 65, '#33FF00', 2, 'solid')
    outbg.place(15, 10)

    #ignore this spaghetti
    button1 = Buttons(root, '1', lambda: buttonpress(1))
    button2 = Buttons(root, '2', lambda: buttonpress(2))
    button3 = Buttons(root, '3', lambda: buttonpress(3))
    button4 = Buttons(root, '4', lambda: buttonpress(4))
    button5 = Buttons(root, '5', lambda: buttonpress(5))
    button6 = Buttons(root, '6', lambda: buttonpress(6))
    button7 = Buttons(root, '7', lambda: buttonpress(7))
    button8 = Buttons(root, '8', lambda: buttonpress(8))
    button9 = Buttons(root, '9', lambda: buttonpress(9))
    button0 = Buttons(root, '0', lambda: buttonpress(0))
    buttonadd = Buttons(root, "+", lambda: buttonpresssign(root, "+"))
    buttonsub = Buttons(root, "-", lambda: buttonpresssign(root, "-"))
    buttondiv = Buttons(root, "/", lambda: buttonpresssign(root, "/"))
    buttonmul = Buttons(root, "*", lambda: buttonpresssign(root, "*"))
    buttonequal = Buttons(root, "=", lambda: buttonpressequal(root))
    button1.place(15, 100)
    button2.place(75, 100)
    button3.place(135, 100)
    button4.place(15, 170)
    button5.place(75, 170)
    button6.place(135, 170)
    button7.place(15, 240)
    button8.place(75, 240)
    button9.place(135, 240)
    buttonadd.place(260, 100)
    buttonsub.place(260, 170)
    buttondiv.place(260, 240)
    buttonmul.place(260, 310)
    buttonequal.place(75, 310)
    button0.place(15,310)

    def buttonpress(dajcyferketykurw):
        global value1, value2, znakpressed
        out = Outputs(value1, 20, 15) #w/o this line, the output is delayed by one number
        #First Input
        if znakpressed == False:
            value1 = str(value1) + str(dajcyferketykurw)
            out = Outputs(value1, 20, 15)
        #Second input
        else:
            outbg = Canvas(root, 280, 65, '#33FF00', 2, 'solid')
            outbg.place(15, 10)
            value2 = str(value2) + str(dajcyferketykurw)
            out = Outputs(value2, 20, 15)


    def buttonpresssign(master, dajznaktykurw):
        global znak, znakpressed
        znak = dajznaktykurw
        znakpressed = True #This variable checks if an operator has been pressed

    def buttonpressequal(master):
        global value1, value2, znak, wynik, znakpressed
        #converting inputs string --> integer
        intval1 = int(value1)
        intval2 = int(value2)

        #Calculations
        if znak == "*":
            wynik = intval1 * intval2
        
        elif znak == "+":
            wynik = intval1 + intval2
        
        elif znak == "-":
            wynik = intval1 - intval2
        
        else:
            wynik = intval1 / intval2
        
        #Output clear
        outbg = Canvas(root, 280, 65, '#33FF00', 2, 'solid')
        outbg.place(15, 10)
        
        out = Outputs(wynik, 20, 15) #Displays the final output   

        #Input and operator check reset
        znakpressed = False
        value1 = ""
        value2 = ""


    root.mainloop()

if __name__ == '__main__':
    main()

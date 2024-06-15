import tkinter as tk
value1 = ""
value2 = ""
znak = ""
znakpressed = False
wynik = 0
equalpressed = False
class Outputs:
    def __init__(self, textvar, x, y):
        self.label = tk.Label(font=('Terminal', 30), text=textvar, bg='#33FF00').place(x=x, y=y)

def Canvas(master, width, height,bg, borderwidth, relief, x, y): 
    tk.Canvas(master, width=width, height=height, bg=bg, borderwidth=borderwidth, relief=relief, highlightthickness=0).place(x=x, y=y)

def main():
    #root
    root = tk.Tk()
    root.geometry('320x380')
    root.title('Kalkulator na infe')
    root.resizable(False, False)
    #backgrounds
    Canvas(root, 325, 455, '#787976', False, 'flat', -1, -1)
    Canvas(root, 280, 65, '#33FF00', 2, 'solid' , 15, 10)

    def Buttoncreate(master, text, x, y):
        tk.Button(master, borderwidth=1, relief='groove', font=("Helvetica", 14), text=text, command=lambda: buttonpress(text), height=2, width=2).place(x=x, y=y)

    text = 0
    x = -45
    y = 100
    for i in range(9):
            text += 1
            x += 60
            if x == 195:
                x = 15
                y = y + 70
            Buttoncreate(root, text, x, y)

    Buttoncreate(root, 0, 15, 310)
    Buttoncreate(root, '+', 260, 100)
    Buttoncreate(root, '-', 260, 170)
    Buttoncreate(root, '*', 260, 240)
    Buttoncreate(root, '/', 260, 310)
    Buttoncreate(root, '=', 75, 310)
    
    def buttonpress(dajcyferketykurw):
        global value1, value2, znakpressed, znak, wynik
        out = Outputs(value1, 20, 15) #w/o this line, the output is delayed by one number
        
        if dajcyferketykurw in ("+", "-", "/", "*"): #operator button pressed
            znak = dajcyferketykurw
            znakpressed = True
 
        elif dajcyferketykurw == "=": #equal button pressed
            intval1 = int(value1)
            intval2 = int(value2)
            
            if znak == "*":
                wynik = intval1 * intval2
            elif znak == "+":
                wynik = intval1 + intval2
            elif znak == "-":
                wynik = intval1 - intval2
            else:
                wynik = intval1 / intval2
            
            Canvas(root, 280, 65, '#33FF00', 2, 'solid',15, 10) #Canvas clear
            out = Outputs(wynik, 20, 15) #Displays the final output   
            znakpressed = False
            value1 = ""
            value2 = ""

        else:
            #Number button pressed
            if znakpressed == False:
                value1 = str(value1) + str(dajcyferketykurw)
                out = Outputs(value1, 20, 15)
                print(value1)
            
            else:                 
                Canvas(root, 280, 65, '#33FF00', 2, 'solid', 15, 10)
                value2 = str(value2) + str(dajcyferketykurw)
                out = Outputs(value2, 20, 15)

    root.mainloop()

if __name__ == '__main__':
    main()

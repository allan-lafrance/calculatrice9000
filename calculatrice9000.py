from tkinter import *

formule = ""
history = []

def click(num):
    global formule
    formule = formule + str(num)
    equation.set(formule)

def equalclick():
    global formule, history
    try:
        result = str(eval(formule))
        history.append(formule + " = " + result)
        equation.set(result)
        formule = result
    except:
        equation.set("error")
        formule = ""

def effacer():
    global formule
    formule = ""
    equation.set("")

#historique

def reset():
    global history
    history = []
    equation.set("")

def show_history():
    global history
    print(history)

#disposition des touches

if __name__ == "__main__":
    master = Tk()
    master.title("Calculatrice")
    master.geometry("375x375")
    equation = StringVar()
    formule_field = Entry(master, textvariable=equation, bg="#fff")
    formule_field.grid(columnspan=4, pady=30, padx=20, ipadx=100, ipady=10)
    history_btn = Button(master, text="Historique", command=show_history, height=2, width=10)
    history_btn.grid(row=1, column=2)
    reset_btn= Button(master, text="Reset", command=reset, height=2, width=10)
    reset_btn.grid(row=1, column=3)
    square= Button(master, text="x²", command=lambda: click("**2"), height=2, width=10)
    square.grid(row=2, column=0)
    square_root= Button(master, text="√x", command=lambda: click("**.5"), height=2, width=10)
    square_root.grid(row=2, column=1)
    effacer = Button(master, text="AC", command=effacer, height=2, width=10) 
    effacer.grid(row=2, column=2)
    divide = Button(master, text=" / ", command=lambda: click("/"), height=2, width=10) 
    divide.grid(row=2, column=3)
    btn_1 = Button(master, text=" 1 ", command=lambda: click(1), height=2, width=10)
    btn_1.grid(row=3, column=0)
    btn_2 = Button(master, text=" 2 ", command=lambda: click(2), height=2, width=10)
    btn_2.grid(row=3, column=1)
    btn_3 = Button(master, text=" 3 ", command=lambda: click(3), height=2, width=10)
    btn_3.grid(row=3, column=2)
    multiply = Button(master, text=" * ", command=lambda: click("*"), height=2, width=10) 
    multiply.grid(row=3, column=3)
    btn_4 = Button(master, text=" 4 ", command=lambda: click(4), height=2, width=10)
    btn_4.grid(row=4, column=0)
    btn_5 = Button(master, text=" 5 ", command=lambda: click(5), height=2, width=10)
    btn_5.grid(row=4, column=1)
    btn_6 = Button(master, text=" 6 ", command=lambda: click(6), height=2, width=10)
    btn_6.grid(row=4, column=2)
    minus = Button(master, text=" - ", command=lambda: click("-"), height=2, width=10) 
    minus.grid(row=4, column=3)
    btn_7 = Button(master, text=" 7 ", command=lambda: click(7), height=2, width=10)
    btn_7.grid(row=5, column=0)
    btn_8 = Button(master, text=" 8 ", command=lambda: click(8), height=2, width=10)
    btn_8.grid(row=5, column=1)
    btn_9 = Button(master, text=" 9 ", command=lambda: click(9), height=2, width=10)
    btn_9.grid(row=5, column=2)
    plus = Button(master, text=" + ", command=lambda: click("+"), height=2, width=10) 
    plus.grid(row=5, column=3)
    percent= Button(master, text="%", command=lambda: click("*100/"), height=2, width=10) 
    percent.grid(row=6, column=0)
    btn_0 = Button(master, text=" 0 ", command=lambda: click(0), height=2, width=10)
    btn_0.grid(row=6, column=1)
    Decimal= Button(master, text=".", command=lambda: click("."), height=2, width=10)
    Decimal.grid(row=6, column=2)
    equal = Button(master, text=" = ", command=equalclick, height=2, width=10, bg="#7F7F7F") 
    equal.grid(row=6, column=3)
    master.mainloop()
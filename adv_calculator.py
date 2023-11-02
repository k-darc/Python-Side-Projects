import tkinter as tk

calculation = ...

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
    except:
        clear_field()

def clear_field():
    global calculation
    calculation = ""

root.mainloop()
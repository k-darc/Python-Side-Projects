import tkinter as tk
import random

def main():
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()

class PongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pong")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="black")

main()
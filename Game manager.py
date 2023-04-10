import tkinter as tk
from tkinter import messagebox
import os

class Manager:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x300")
        self.window.config(bg="#fb551c")
        self.window.title("Idle Game")

        tk.Label(self.window, text="Lobster Manager", font=("Consolas", 40, "bold"), bg="#fb551c").pack(fill="x", pady=10)

        self.download = tk.Button(self.window, command=self.func_download, text="DOWNLOAD GAME", font=("Fixedsys", 20, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").pack(pady=5)
        self.update = tk.Button(self.window, command=self.func_update, text="UPDATE GAME", font=("Fixedsys", 20, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").pack(pady=5)
        self.delete = tk.Button(self.window, command=self.func_delete, text="DELETE GAME FILES", font=("Fixedsys", 20, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").pack(pady=5)
        self.window.mainloop()
    
    def func_download(self):
        pass

    def func_update(self):
        pass

    def func_delete(self):
        pass

Manager()
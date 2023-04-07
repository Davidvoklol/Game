import tkinter as tk
from tkinter import messagebox
import os


window = tk.Tk()
window.geometry("500x300")
window.config(bg="gray")
window.title("Manager")

tk.Label(window, text="Game Manager", font=("Consolas", 40, "bold"), bg="gray").pack(fill="x", pady=10)

download = tk.Button(window, text="Download Game", font=("Fixedsys", 20, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").pack(pady=5)
delete = tk.Button(window, text="Delete Game", font=("Fixedsys", 20, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").pack(pady=5)
window.mainloop()
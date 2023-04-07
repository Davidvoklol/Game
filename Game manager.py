import tkinter as tk
from tkinter import messagebox
import os

class Manager:
    def __init__(self):
        self.path = os.path.abspath("Game manager.py")
        if os.path.exists("C:/Users/user"):
            self.game_path = "C:/Users/user/Idle Lobster"
    def Download(self):
        print(self.path)
        print(self.game_path)
    def Update():
        pass
    def Delete():
        pass




window = tk.Tk()
window.geometry("500x300")
window.config(bg="#fb551c")
window.title("Idle Game")

tk.Label(window, text="Lobster Manager", font=("Consolas", 40, "bold"), bg="#fb551c").pack(fill="x", pady=10)

download = tk.Button(window, text="DOWNLOAD GAME", font=("Fixedsys", 20, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").pack(pady=5)
update = tk.Button(window, text="UPDATE GAME", font=("Fixedsys", 20, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").pack(pady=5)
delete = tk.Button(window, text="DELETE GAME FILES", font=("Fixedsys", 20, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").pack(pady=5)
window.mainloop()
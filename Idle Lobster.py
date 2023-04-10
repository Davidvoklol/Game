import tkinter as tk
from tkinter import messagebox
from data.default_data import *
from data.user_data import *

class User():
    def __init__(user):
        pass

class Game:
    def __init__(self, bg):
        self.bg = bg

        #   Game Setup
        self.window = tk.Tk()
        self.window.geometry("1600x1000")
        self.window.config(bg=self.bg)
        self.window.title("Idle Game")
        #   Game Setup

        #   Header
        self.header = tk.Frame(self.window, bg=self.bg)
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=1)
        self.header.pack(fill="x", padx=30, pady=20)
        tk.Label(self.header, text="Idle Lobster", bg=self.bg, font=("Terminal", 50, "bold")).grid(row=0, columnspan=2, sticky=tk.W + tk.E)
        self.frame_money = tk.Frame(self.header, bg="black")
        self.frame_money.grid(row=1, column=0, sticky=tk.W)
        self.display_money = tk.Label(self.frame_money, text="Money: " + str(cash) + "$", bg=self.bg, font=("Terminal", 25, "bold")).pack(padx=3, pady=3)
        self.frame_lobster = tk.Frame(self.header, bg="black")
        self.frame_lobster.grid(row=1, column=1, sticky=tk.E)
        self.display_lobster = tk.Label(self.frame_lobster, text="Lobsters: 0$", bg=self.bg, font=("Terminal", 25, "bold")).pack(padx=3, pady=3)
        #   Header


        #   Game Platform
        self.game_platform = tk.Frame(self.window, bg=self.bg)
        self.game_platform.columnconfigure(0, weight=1)
        self.game_platform.columnconfigure(1, weight=1)
        self.game_platform.columnconfigure(2, weight=1)
        self.game_platform.pack(fill="x", padx=50, pady=20)
        #   Game Platform


        #   Platform0
        self.platform0 = tk.Frame(self.game_platform, bg=self.bg)
        self.platform0.columnconfigure(0, weight=1)
        self.platform0.columnconfigure(1, weight=1)
        self.platform0.columnconfigure(2, weight=1)
        self.platform0.columnconfigure(3, weight=1)
        self.platform0.grid(row=0, column=0, sticky=tk.W + tk.E)
        #   Platform0


        #   Platform1
        self.platform1 = tk.Frame(self.game_platform, bg=self.bg)
        self.platform1.columnconfigure(0, weight=1)
        self.platform1.columnconfigure(1, weight=1)
        self.platform1.columnconfigure(2, weight=1)
        self.platform1.columnconfigure(3, weight=1)
        self.platform1.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.button_taptap = tk.Button(self.platform1, command=self.taptap, text="0$ / TAP", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=0, columnspan=4, sticky=tk.W + tk.E, pady=5)
        self.label_taptap = tk.Label(self.platform1, text="TapTap Lobster: lvl 0", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d").grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_upgrade_taptap = tk.Button(self.platform1, text="Upgrade: 000$", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=1, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_autotap = tk.Button(self.platform1, text="UNLOCK LOBSTERS: 000$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=2, columnspan=4, sticky=tk.W + tk.E, pady=5)
        
        self.label_bob = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d").grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_bob = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=3, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.label_doodle = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d").grid(row=4, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_doodle = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=4, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.label_winky = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d").grid(row=5, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_winky = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=5, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.label_fred = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d").grid(row=6, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_fred = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=6, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.label_giggles = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d").grid(row=7, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_giggles = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=7, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.label_larry = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d").grid(row=8, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_larry = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=8, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.frame_david = tk.Frame(self.platform1, bg="black")
        self.frame_david.columnconfigure(0, weight=1)
        self.frame_david.columnconfigure(1, weight=1)
        self.frame_david.grid(row=10, columnspan=4, sticky=tk.W + tk.E, pady=35)
        
        self.label_david = tk.Label(self.frame_david, text="Secret Lobster...", height=3, width=1, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d").grid(row=0, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.button_david = tk.Button(self.frame_david, text="---------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white").grid(row=0, column=1, sticky=tk.W + tk.E, padx=5, pady=5)
        #   Platform1


        #   Platform2
        self.platform2 = tk.Frame(self.game_platform, bg=self.bg)
        self.platform2.columnconfigure(0, weight=1)
        self.platform2.columnconfigure(1, weight=1)
        self.platform2.columnconfigure(2, weight=1)
        self.platform2.columnconfigure(3, weight=1)
        self.platform2.grid(row=0, column=2, sticky=tk.W + tk.E)
        #   Platform2

        self.window.mainloop()

    def taptap(self):
        pass

    def check_values(self):
        with open("data/user_data.py") as f:
            print(f.read())



Game("#fb551c")


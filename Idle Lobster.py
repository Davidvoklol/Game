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
        self.display_money = tk.Label(self.frame_money, text="Money: " + str(cash) + "$", bg=self.bg, font=("Terminal", 25, "bold"))
        self.display_money.pack(padx=3, pady=3)
        self.frame_lobster = tk.Frame(self.header, bg="black")
        self.frame_lobster.grid(row=1, column=1, sticky=tk.E)
        self.display_lobster = tk.Label(self.frame_lobster, text="Golden Lobsters: " + str(golden_lobster), bg=self.bg, font=("Terminal", 25, "bold"))
        self.display_lobster.pack(padx=3, pady=3)
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

        self.button_taptap = tk.Button(self.platform1, command=self.taptap, text=str(round(tap_value, 2)) + "$ / TAP", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_taptap.grid(row=0, columnspan=4, sticky=tk.W + tk.E, pady=5)
        self.label_taptap = tk.Label(self.platform1, text="TapTap Lobster: lvl " + str(tap_lvl), height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_taptap.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_upgrade_taptap = tk.Button(self.platform1, command=self.tap_upgrade, text="Upgrade: " + str(round(tap_upgrade_cost, 2)) + "$", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_upgrade_taptap.grid(row=1, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_bob = tk.Button(self.platform1, command=self.bob_purchase, text="UNLOCK A NEW LOBSTER: " + str(bob_unlcok_cost) + "$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_unlock_bob.grid(row=2, columnspan=4, sticky=tk.W + tk.E, pady=5)
        
        self.label_bob = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_bob.grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_bob = tk.Button(self.platform1, command=self.bob_upgrade, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_bob.grid(row=3, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_doodle = tk.Button(self.platform1, command=self.doodle_purchase, text="UNLOCK A NEW LOBSTER: " + str(doodle_unlcok_cost) + "$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")

        self.label_doodle = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_doodle.grid(row=5, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_doodle = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_doodle.grid(row=5, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_winky = tk.Button(self.platform1, command=self.winky_purchase, text="UNLOCK A NEW LOBSTER: " + str(doodle_unlcok_cost) + "$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        
        self.label_winky = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_winky.grid(row=7, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_winky = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_winky.grid(row=7, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.label_fred = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_fred.grid(row=9, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_fred = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_fred.grid(row=9, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.label_giggles = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_giggles.grid(row=11, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_giggles = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_giggles.grid(row=11, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.label_larry = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_larry.grid(row=13, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_larry = tk.Button(self.platform1, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_larry.grid(row=13, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.frame_david = tk.Frame(self.platform1, bg="black")
        self.frame_david.columnconfigure(0, weight=1)
        self.frame_david.columnconfigure(1, weight=1)
        self.frame_david.grid(row=15, columnspan=4, sticky=tk.W + tk.E, pady=35)
        
        self.label_david = tk.Label(self.frame_david, text="Secret Lobster...", height=3, width=1, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
        self.label_david.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5, pady=5)
        self.button_david = tk.Button(self.frame_david, text="---------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_david.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5, pady=5)
        #   Platform1


        #   Platform2
        self.platform2 = tk.Frame(self.game_platform, bg=self.bg)
        self.platform2.columnconfigure(0, weight=1)
        self.platform2.columnconfigure(1, weight=1)
        self.platform2.columnconfigure(2, weight=1)
        self.platform2.columnconfigure(3, weight=1)
        self.platform2.grid(row=0, column=2, sticky=tk.W + tk.E)
        #   Platform2

        self.check_upgrades()
        self.window.mainloop()
    
    
    
    
    def check_upgrades(self):
        global cash, tap_upgrade_cost, bob_unlcok_cost, doodle_unlcok_cost, doodle_state

        if cash >= tap_upgrade_cost:
            self.button_upgrade_taptap.config(state="active")
        else:
            self.button_upgrade_taptap.config(state="disabled")

        # bob
        if cash >= bob_unlcok_cost and bob_state == "active":
            self.button_unlock_bob.config(state="active")
        elif cash < bob_unlcok_cost and bob_state == "active":
            self.button_unlock_bob.config(state="disabled")

        if cash >= bob_upgrade_cost and bob_state == "destroyed":
            self.button_bob.config(state="active")
        else:
            self.button_bob.config(state="disabled")

        # doodle
        if cash >= doodle_unlcok_cost and doodle_state == "active":
            self.button_unlock_doodle.config(state="active")
        elif cash < doodle_unlcok_cost and doodle_state == "active":
            self.button_unlock_doodle.config(state="disabled")

        if cash >= doodle_upgrade_cost and doodle_state == "destroyed":
            self.button_doodle.config(state="active")
        else:
            self.button_doodle.config(state="disabled")

        # winky


    def taptap(self):
        global cash, tap_value
        cash += tap_value
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.check_upgrades()
    
    def tap_upgrade(self):
        global cash, tap_upgrade_cost, tap_lvl, tap_value
        cash -= tap_upgrade_cost
        tap_lvl += 1
        tap_value += tap_lvl * 1.5
        tap_upgrade_cost = tap_value * 3 + (tap_lvl * tap_value)
        self.label_taptap.config(text="TapTap Lobster: lvl " + str(tap_lvl))
        self.button_upgrade_taptap.config(text="Upgrade: " + str(round(tap_upgrade_cost, 2)) + "$")
        self.button_taptap.config(text=str(round(tap_value, 2)) + "$ / TAP")
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.check_upgrades()
    
    def bob_purchase(self):
        global cash, bob_unlcok_cost, bob_state
        cash -= bob_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.button_unlock_bob.destroy()
        self.button_unlock_doodle.grid(row=4, columnspan=4, sticky=tk.W + tk.E, pady=5)
        bob_state = "destroyed"
        self.label_bob.config(text="Bob Lobster: lvl " + str(bob_lvl))
        self.button_bob.config(text="Upgrade: " + str(round(bob_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.bob_earning()
    
    def bob_earning(self):
        global cash, bob_value
        cash += bob_value
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.window.after(1000, self.bob_earning)
        self.check_upgrades()

    def bob_upgrade(self):
        global bob_lvl, bob_upgrade_cost, cash, bob_value, bob_unlcok_cost
        cash -= bob_upgrade_cost
        bob_lvl += 1
        bob_value = bob_unlcok_cost / 500 * bob_lvl
        bob_upgrade_cost = bob_value * bob_lvl * 100
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.label_bob.config(text="Bob Lobster: lvl " + str(bob_lvl))
        self.button_bob.config(text="Upgrade: " + str(round(bob_upgrade_cost, 2)) + "$")
        self.check_upgrades()
    
    def doodle_purchase(self):
        global cash, doodle_unlcok_cost, doodle_state
        cash -= doodle_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.button_unlock_doodle.destroy()
        self.button_unlock_winky.grid(row=6, columnspan=4, sticky=tk.W + tk.E, pady=5)
        doodle_state = "destroyed"
        self.label_doodle.config(text="doodle Lobster: lvl " + str(doodle_lvl))
        self.button_doodle.config(text="Upgrade: " + str(round(doodle_upgrade_cost, 2)) + "$")
        self.check_upgrades()

    def doodle_upgrade(self):
        global doodle_lvl, doodle_upgrade_cost, cash, doodle_value, doodle_unlcok_cost
        cash -= doodle_upgrade_cost
        doodle_lvl += 1
        doodle_value = doodle_unlcok_cost / 500 * doodle_lvl
        doodle_upgrade_cost = doodle_value * doodle_lvl * 100
        self.display_money.config(text="MOney: " + str(round(cash, 2)) + "$")
        self.label_doodle.config(text="doodle Lobster: lvl " + str(doodle_lvl))
        self.button_doodle.config(text="Upgrade: " + str(round(doodle_upgrade_cost, 2)) + "$")
        self.check_upgrades()

    def winky_purchase():
        pass

        






Game("#fb551c")


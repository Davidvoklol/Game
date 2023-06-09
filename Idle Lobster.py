import tkinter as tk
from tkinter import messagebox
from data.default_data import *
from data.user_data import *

class User():
    def __init__(user):
        user.window = tk.Tk()
        user.window.title("Beginning")
        user.window.geometry("500x250")
        user.title = tk.Label()
        user.window.mainloop()

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
        self.game_platform.columnconfigure(3, weight=1)
        self.game_platform.columnconfigure(4, weight=1)
        self.game_platform.pack(fill="x")
        #   Game Platform


        #   Platform0
        self.platform0 = tk.Frame(self.game_platform, bg=self.bg)
        self.platform0.columnconfigure(0, weight=1)
        self.platform0.columnconfigure(1, weight=1)
        self.platform0.grid(row=0, column=0, sticky=tk.W + tk.N + tk.S, padx=40)

        self.button_save = tk.Button(self.platform0, text="Save game", font=("Terminal", 15, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").grid(row=0, column=1, sticky= tk.W + tk.E, pady=5, padx=5)
        self.button_settings = tk.Button(self.platform0, text="Settings", font=("Terminal", 15, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").grid(row=0, column=0, sticky= tk.W + tk.E, pady=5)
        self.button_stats = tk.Button(self.platform0, text="Stats", font=("Terminal", 15, "bold"), bg="black", activebackground="black", fg="white", activeforeground="white").grid(row=1, column=0, columnspan=2, sticky= tk.W + tk.E, pady=5)
        self.label_autolobsters_earning = tk.Label(self.platform0, text="Auto / sec: $$$", font=("Segoe Print", 11, "bold"), bg=self.bg, relief="solid")
        self.label_bob_earning = tk.Label(self.platform0, text="Bob / sec: $$$", font=("Segoe Print", 11, "bold"), bg=self.bg, relief="solid")
        self.label_doodle_earning = tk.Label(self.platform0, text="Doodle / sec: $$$", font=("Segoe Print", 11, "bold"), bg=self.bg, relief="solid")
        self.label_winky_earning = tk.Label(self.platform0, text="Winky / sec: $$$", font=("Segoe Print", 11, "bold"), bg=self.bg, relief="solid")
        self.label_fred_earning = tk.Label(self.platform0, text="Fred / sec: $$$", font=("Segoe Print", 11, "bold"), bg=self.bg, relief="solid")
        self.label_giggles_earning = tk.Label(self.platform0, text="Giggles / sec: $$$", font=("Segoe Print", 11, "bold"), bg=self.bg, relief="solid")
        self.label_larry_earning = tk.Label(self.platform0, text="Larry / sec: $$$", font=("Segoe Print", 11, "bold"), bg=self.bg, relief="solid")
        self.label_david_earning = tk.Label(self.platform0, text="David / sec: $$$", font=("Segoe Print", 11, "bold"), bg=self.bg, relief="solid")
        #   Platform0


        #   Platform1
        self.platform1 = tk.Frame(self.game_platform, bg=self.bg)
        self.platform1.columnconfigure(0, weight=1)
        self.platform1.columnconfigure(1, weight=1)
        self.platform1.columnconfigure(2, weight=1)
        self.platform1.columnconfigure(3, weight=1)
        self.platform1.grid(row=0, column=1, columnspan=2, sticky=tk.W + tk.E + tk.N + tk.S, padx=10)

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
        self.button_doodle = tk.Button(self.platform1, command=self.doodle_upgrade, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_doodle.grid(row=5, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_winky = tk.Button(self.platform1, command=self.winky_purchase, text="UNLOCK A NEW LOBSTER: " + str(winky_unlcok_cost) + "$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        
        self.label_winky = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_winky.grid(row=7, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_winky = tk.Button(self.platform1, command=self.winky_upgrade, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_winky.grid(row=7, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_fred = tk.Button(self.platform1, command=self.fred_purchase, text="UNLOCK A NEW LOBSTER: " + str(fred_unlcok_cost) + "$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")

        self.label_fred = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_fred.grid(row=9, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_fred = tk.Button(self.platform1, command=self.fred_upgrade, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_fred.grid(row=9, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_giggles = tk.Button(self.platform1, command=self.giggles_purchase, text="UNLOCK A NEW LOBSTER: " + str(giggles_unlcok_cost) + "$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")

        self.label_giggles = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_giggles.grid(row=11, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_giggles = tk.Button(self.platform1, command=self.giggles_upgrade, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_giggles.grid(row=11, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_larry = tk.Button(self.platform1, command=self.larry_purchase, text="UNLOCK A NEW LOBSTER: " + str(larry_unlcok_cost) + "$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")

        self.label_larry = tk.Label(self.platform1, text="Lobster: ---", height=3, width=1, font=("Courier", 14, "bold"), relief="solid", bg="#cc562d")
        self.label_larry.grid(row=13, column=0, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        self.button_larry = tk.Button(self.platform1, command=self.larry_upgrade, text="--------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_larry.grid(row=13, column=2, columnspan=2, sticky=tk.W + tk.E, padx=2.5)
        
        self.button_unlock_david = tk.Button(self.platform1, command=self.david_purchase, text="UNLOCK A NEW LOBSTER: " + str(david_unlcok_cost) + "$", height=2, width=1, font=("Lucida Console", 20, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")

        self.frame_david = tk.Frame(self.platform1, bg="black")
        self.frame_david.columnconfigure(0, weight=1)
        self.frame_david.columnconfigure(1, weight=1)
        self.frame_david.grid(row=15, columnspan=4, sticky=tk.W + tk.E, pady=35)
        
        self.label_david = tk.Label(self.frame_david, text="Secret Lobster...", height=3, width=1, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
        self.label_david.grid(row=0, column=0, sticky=tk.W + tk.E, pady=5)
        self.button_david = tk.Button(self.frame_david, command=self.david_upgrade, text="---------", height=2, width=1, font=("Courier", 14, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
        self.button_david.grid(row=0, column=1, sticky=tk.W + tk.E, pady=5)
        #   Platform1


        #   Platform2
        self.platform2 = tk.Frame(self.game_platform, bg=self.bg)
        self.platform2.columnconfigure(0, weight=1)
        self.platform2.columnconfigure(1, weight=1)
        self.platform2.columnconfigure(2, weight=1)
        self.platform2.columnconfigure(3, weight=1)
        self.platform2.grid(row=0, column=4, sticky=tk. W + tk.E + tk.N + tk.S)
        #   Platform2

        self.check_upgrades()
        self.window.mainloop()
    
    
    
    
    def check_upgrades(self):

        if cash >= tap_upgrade_cost:
            self.button_upgrade_taptap.config(state="active")
        else:
            self.button_upgrade_taptap.config(state="disabled")

        # bob purchase
        if cash >= bob_unlcok_cost and bob_state == "active":
            self.button_unlock_bob.config(state="active")
        elif cash < bob_unlcok_cost and bob_state == "active":
            self.button_unlock_bob.config(state="disabled")
        # bob upgrade
        if cash >= bob_upgrade_cost and bob_state == "destroyed":
            self.button_bob.config(state="active")
        else:
            self.button_bob.config(state="disabled")

        # doodle purchase
        if cash >= doodle_unlcok_cost and doodle_state == "active":
            self.button_unlock_doodle.config(state="active")
        elif cash < doodle_unlcok_cost and doodle_state == "active":
            self.button_unlock_doodle.config(state="disabled")
        # doodle upgrade
        if cash >= doodle_upgrade_cost and doodle_state == "destroyed":
            self.button_doodle.config(state="active")
        else:
            self.button_doodle.config(state="disabled")

        # winky purchase
        if cash >= winky_unlcok_cost and winky_state == "active":
            self.button_unlock_winky.config(state="active")
        elif cash < winky_unlcok_cost and winky_state == "active":
            self.button_unlock_winky.config(state="disabled")
        # winky upgrade
        if cash >= winky_upgrade_cost and winky_state == "destroyed":
            self.button_winky.config(state="active")
        else:
            self.button_winky.config(state="disabled")
        
        # fred purchase
        if cash >= fred_unlcok_cost and fred_state == "active":
            self.button_unlock_fred.config(state="active")
        elif cash < fred_unlcok_cost and fred_state == "active":
            self.button_unlock_fred.config(state="disabled")
        # fred upgrade
        if cash >= fred_upgrade_cost and fred_state == "destroyed":
            self.button_fred.config(state="active")
        else:
            self.button_fred.config(state="disabled")

        # giggles purchase
        if cash >= giggles_unlcok_cost and giggles_state == "active":
            self.button_unlock_giggles.config(state="active")
        elif cash < giggles_unlcok_cost and giggles_state == "active":
            self.button_unlock_giggles.config(state="disabled")
        # giggles upgrade
        if cash >= giggles_upgrade_cost and giggles_state == "destroyed":
            self.button_giggles.config(state="active")
        else:
            self.button_giggles.config(state="disabled")

        # larry purchase
        if cash >= larry_unlcok_cost and larry_state == "active":
            self.button_unlock_larry.config(state="active")
        elif cash < larry_unlcok_cost and larry_state == "active":
            self.button_unlock_larry.config(state="disabled")
        # larry upgrade
        if cash >= larry_upgrade_cost and larry_state == "destroyed":
            self.button_larry.config(state="active")
        else:
            self.button_larry.config(state="disabled")
        
        # david purchase
        if cash >= david_unlcok_cost and david_state == "active":
            self.button_unlock_david.config(state="active")
        elif cash < david_unlcok_cost and david_state == "active":
            self.button_unlock_david.config(state="disabled")
        # david upgrade
        if cash >= david_upgrade_cost and david_state == "destroyed":
            self.button_david.config(state="active")
        else:
            self.button_david.config(state="disabled")
    
    def earning_matters_update(self):
        self.label_bob_earning.config(text="Bob / sec: " + str(round(bob_value, 2)) + "$")
        self.label_doodle_earning.config(text="Doodle / sec: " + str(round(doodle_value, 2)) + "$")
        self.label_winky_earning.config(text="Winky / sec: " + str(round(winky_value, 2)) + "$")
        self.label_fred_earning.config(text="Fred / sec: " + str(round(fred_value, 2)) + "$")
        self.label_giggles_earning.config(text="Giggles / sec: " + str(round(giggles_value, 2)) + "$")
        self.label_larry_earning.config(text="Larry / sec: " + str(round(larry_value, 2)) + "$")
        self.label_david_earning.config(text="David / sec: " + str(int(david_value)))


    def taptap(self):
        global cash, tap_value
        cash += tap_value
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.check_upgrades()
    
    def tap_upgrade(self):
        global cash, tap_upgrade_cost, tap_lvl, tap_value
        cash -= tap_upgrade_cost
        tap_lvl += 1
        tap_value += tap_lvl * 0.5
        tap_upgrade_cost = tap_value * 5 + tap_lvl ** 2.6
        self.label_taptap.config(text="TapTap Lobster: lvl " + str(tap_lvl))
        self.button_upgrade_taptap.config(text="Upgrade: " + str(round(tap_upgrade_cost, 2)) + "$")
        self.button_taptap.config(text=str(round(tap_value, 2)) + "$ / TAP")
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.check_upgrades()

     # BOB
    def bob_purchase(self):
        global cash, bob_unlcok_cost, bob_state
        cash -= bob_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.button_unlock_bob.destroy()
        self.button_unlock_doodle.grid(row=4, columnspan=4, sticky=tk.W + tk.E, pady=5)
        self.label_autolobsters_earning.grid(row=2, columnspan=2, pady=20, sticky=tk.W + tk.E)
        self.label_bob_earning.grid(row=3, columnspan=2, pady=20, sticky=tk.W + tk.E)
        bob_state = "destroyed"
        self.label_bob.config(text="Bob Lobster: lvl " + str(bob_lvl))
        self.button_bob.config(text="Upgrade: " + str(round(bob_upgrade_cost, 2)) + "$")
        self.bob_earning()
        self.earning_matters_update()
    
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
        bob_value = (bob_lvl / 2) ** 2
        bob_upgrade_cost = bob_value * 60 + bob_lvl ** 3.32
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.label_bob.config(text="Bob Lobster: lvl " + str(bob_lvl))
        self.button_bob.config(text="Upgrade: " + str(round(bob_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.earning_matters_update()
    
    # DOODLE
    def doodle_purchase(self):
        global cash, doodle_unlcok_cost, doodle_state
        cash -= doodle_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.button_unlock_doodle.destroy()
        self.button_unlock_winky.grid(row=6, columnspan=4, sticky=tk.W + tk.E, pady=5)
        self.label_doodle_earning.grid(row=4, columnspan=2, pady=20, sticky=tk.W + tk.E)
        doodle_state = "destroyed"
        self.label_doodle.config(text="Doodle Lobster: lvl " + str(doodle_lvl))
        self.button_doodle.config(text="Upgrade: " + str(round(doodle_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.earning_matters_update()
    
    def doodle_earning(self):
        global cash, doodle_value
        cash += bob_value
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.window.after(1000, self.doodle_earning)
        self.check_upgrades()

    def doodle_upgrade(self):
        global doodle_lvl, doodle_upgrade_cost, cash, doodle_value, doodle_unlcok_cost
        cash -= doodle_upgrade_cost
        doodle_lvl += 1
        doodle_value = ((doodle_lvl / 2) ** 2) * 2.2
        doodle_upgrade_cost = doodle_value * 60 + doodle_lvl ** 3.581
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.label_doodle.config(text="Doodle Lobster: lvl " + str(doodle_lvl))
        self.button_doodle.config(text="Upgrade: " + str(round(doodle_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.earning_matters_update()

    # WINKY
    def winky_purchase(self):
        global cash, winky_unlcok_cost, winky_state
        cash -= winky_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.button_unlock_winky.destroy()
        self.button_unlock_fred.grid(row=8, columnspan=4, sticky=tk.W + tk.E, pady=5)
        self.label_winky_earning.grid(row=5, columnspan=2, pady=20, sticky=tk.W + tk.E)
        winky_state = "destroyed"
        self.label_winky.config(text="Winky Lobster: lvl " + str(winky_lvl))
        self.button_winky.config(text="Upgrade: " + str(round(winky_upgrade_cost, 2)) + "$")
        self.winky_earning()
        self.earning_matters_update()
    
    def winky_earning(self):
        global cash, winky_value
        cash += winky_value
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.window.after(1000, self.winky_earning)
        self.check_upgrades()
    
    def winky_upgrade(self):
        global winky_lvl, winky_upgrade_cost, cash, winky_value, winky_unlcok_cost
        cash -= winky_upgrade_cost
        winky_lvl += 1
        winky_value = ((winky_lvl / 2) ** 2) * 3.6
        winky_upgrade_cost = winky_value * 60 + winky_lvl ** 3.752
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.label_winky.config(text="Winky Lobster: lvl " + str(winky_lvl))
        self.button_winky.config(text="Upgrade: " + str(round(winky_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.earning_matters_update()
    
    # FRED
    def fred_purchase(self):
        global cash, fred_unlcok_cost, fred_state
        cash -= fred_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.button_unlock_fred.destroy()
        self.button_unlock_giggles.grid(row=10, columnspan=4, sticky=tk.W + tk.E, pady=5)
        self.label_fred_earning.grid(row=6, columnspan=2, pady=20, sticky=tk.W + tk.E)
        fred_state = "destroyed"
        self.label_fred.config(text="Fred Lobster: lvl " + str(fred_lvl))
        self.button_fred.config(text="Upgrade: " + str(round(fred_upgrade_cost, 2)) + "$")
        self.fred_earning()
        self.earning_matters_update()

    def fred_earning(self):
        global cash, fred_value
        cash += fred_value
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.window.after(1000, self.fred_earning)
        self.check_upgrades()
    
    def fred_upgrade(self):
        global fred_lvl, fred_upgrade_cost, cash, fred_value, fred_unlcok_cost
        cash -= fred_upgrade_cost
        fred_lvl += 1
        fred_value = ((fred_lvl / 2) ** 2) * 5.2
        fred_upgrade_cost = fred_value * 60 + fred_lvl ** 3.881
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.label_fred.config(text="Fred Lobster: lvl " + str(fred_lvl))
        self.button_fred.config(text="Upgrade: " + str(round(fred_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.earning_matters_update()
    
    # GIGGLES
    def giggles_purchase(self):
        global cash, giggles_unlcok_cost, giggles_state
        cash -= giggles_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.button_unlock_giggles.destroy()
        self.button_unlock_larry.grid(row=12, columnspan=4, sticky=tk.W + tk.E, pady=5)
        self.label_giggles_earning.grid(row=7, columnspan=2, pady=20, sticky=tk.W + tk.E)
        giggles_state = "destroyed"
        self.label_giggles.config(text="Giggles Lobster: lvl " + str(giggles_lvl))
        self.button_giggles.config(text="Upgrade: " + str(round(giggles_upgrade_cost, 2)) + "$")
        self.giggles_earning()
        self.earning_matters_update()

    def giggles_earning(self):
        global cash, giggles_value
        cash += giggles_value
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.window.after(1000, self.giggles_earning)
        self.check_upgrades()
    
    def giggles_upgrade(self):
        global giggles_lvl, giggles_upgrade_cost, cash, giggles_value, giggles_unlcok_cost
        cash -= giggles_upgrade_cost
        giggles_lvl += 1
        giggles_value = ((giggles_lvl / 2) ** 2) * 7
        giggles_upgrade_cost = giggles_value * 60 + giggles_lvl ** 4.009
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.label_giggles.config(text="Giggles Lobster: lvl " + str(giggles_lvl))
        self.button_giggles.config(text="Upgrade: " + str(round(giggles_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.earning_matters_update()
    
    # LARRY
    def larry_purchase(self):
        global cash, larry_unlcok_cost, larry_state
        cash -= larry_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.button_unlock_larry.destroy()
        self.button_unlock_david.grid(row=14, columnspan=4, sticky=tk.W + tk.E, pady=5)
        self.label_larry_earning.grid(row=8, columnspan=2, pady=20, sticky=tk.W + tk.E)
        larry_state = "destroyed"
        self.label_larry.config(text="Larry Lobster: lvl " + str(larry_lvl))
        self.button_larry.config(text="Upgrade: " + str(round(larry_upgrade_cost, 2)) + "$")
        self.larry_earning()
        self.earning_matters_update()

    def larry_earning(self):
        global cash, larry_value
        cash += larry_value
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.window.after(1000, self.larry_earning)
        self.check_upgrades()
    
    def larry_upgrade(self):
        global larry_lvl, larry_upgrade_cost, cash, larry_value, larry_unlcok_cost
        cash -= larry_upgrade_cost
        larry_lvl += 1
        larry_value = ((larry_lvl / 2) ** 2) * 9
        larry_upgrade_cost = larry_value * 60 + larry_lvl ** 4.094
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.label_larry.config(text="Larry Lobster: lvl " + str(larry_lvl))
        self.button_larry.config(text="Upgrade: " + str(round(larry_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.earning_matters_update()
    
    # DAVID
    def david_purchase(self):
        global cash, david_unlcok_cost, david_state
        cash -= david_unlcok_cost
        self.display_money.config(text="Money: " + str(round(cash, 2)))
        self.label_david_earning.grid(row=9, columnspan=2, pady=60, sticky=tk.W + tk.E)
        self.button_unlock_david.destroy()
        david_state = "destroyed"
        self.label_david.config(text="David Lobster: lvl " + str(david_lvl))
        self.button_david.config(text="Upgrade: " + str(round(david_upgrade_cost, 2)) + "$")
        self.david_earning()
        self.earning_matters_update()
    
    def david_earning(self):
        global cash, david_value, golden_lobster
        golden_lobster += david_value
        self.display_lobster.config(text="Golden Lobsters: " + str(int(golden_lobster)))
        self.window.after(1000, self.david_earning)
        self.check_upgrades()
    
    def david_upgrade(self):
        global david_lvl, david_upgrade_cost, cash, david_value, david_unlcok_cost
        cash -= david_upgrade_cost
        david_lvl += 1
        david_value = david_lvl ** 0.805
        david_upgrade_cost = david_upgrade_cost = (david_lvl * 100) ** 2.5
        self.display_money.config(text="Money: " + str(round(cash, 2)) + "$")
        self.label_david.config(text="David Lobster: lvl " + str(david_lvl))
        self.button_david.config(text="Upgrade: " + str(round(david_upgrade_cost, 2)) + "$")
        self.check_upgrades()
        self.earning_matters_update()

    


Game("#fb551c")
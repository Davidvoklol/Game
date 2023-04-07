import tkinter as tk
from tkinter import messagebox
from data.default_data import *
from data.user_data import *
import os



bg = "#fb551c"
#   game set up{
game = tk.Tk()
game.geometry("1600x1000")
game.title("Idle Lobster")
game.config(bg=bg)
#   }#game set up


#   Functions{
#   }Functions


#   header zone{
header = tk.Frame(game, bg=bg)
header.columnconfigure(0, weight=1)
header.pack(fill="x", padx=15, pady=10)

title = tk.Label(header, text="Idle Lobster", bg=bg, font=("Terminal", 50, "bold"))
title.grid(row=0, columnspan=2, sticky=tk.W + tk.E)

labelfrane_money = tk.Frame(header, bg="black")
labelfrane_money.grid(row=1, column=0, sticky=tk.W)

display_money = tk.Label(labelfrane_money, text="Money: 0$", bg=bg, font=("Terminal", 23, "bold"))
display_money.pack(padx=3, pady=3)

labelfrane_lobster = tk.Frame(header, bg="black")
labelfrane_lobster.grid(row=1, column=1, sticky=tk.E)

display_lobster = tk.Label(labelfrane_lobster, text="Golden Lobsters: 0", bg=bg, font=("Terminal", 23, "bold"))
display_lobster.pack(padx=3, pady=3)
#   }header zone


# game platfrom set up{
main_game_platform = tk.Frame(game, bg=bg)
main_game_platform.columnconfigure(0, weight=1)
main_game_platform.columnconfigure(1, weight=1)
main_game_platform.columnconfigure(2, weight=1)
main_game_platform.pack(fill="x" ,padx=15, pady=15)



game_platform0 = tk.Frame(main_game_platform , bg=bg)
game_platform0.columnconfigure(0, weight=1)
game_platform0.columnconfigure(1, weight=1)
game_platform0.columnconfigure(2, weight=1)
game_platform0.grid(row=0, column=0, sticky=tk.E + tk.W + tk.S + tk.N)

game_platform1 = tk.Frame(main_game_platform, bg=bg)
game_platform1.columnconfigure(0, weight=1)
game_platform1.columnconfigure(1, weight=1)
game_platform1.columnconfigure(2, weight=1)
game_platform1.grid(row=0, column=1)

game_platform2 = tk.Frame(main_game_platform , bg=bg)
game_platform2.columnconfigure(0,weight=1)
game_platform2.grid(row=0, column=2, sticky=tk.E + tk.W + tk.S + tk.N)
#   }game platfrom set up

#   Game_Platform0{
game_save = tk.Button(game_platform0, text="Save", font=("Courier", 12, "bold"), bg="black", fg="white", activebackground="black", activeforeground="white")
game_save.grid(row=0, column=0, sticky=tk.W + tk.E, padx=5, pady=10)

auto_save = tk.Button(game_platform0, text="Auto Save:OFF", font=("Courier", 12, "bold"), bg="black", fg="white", activebackground="black", activeforeground="white")
auto_save.grid(row=0, column=1, columnspan=2, sticky=tk.W + tk.E, pady=10)

lobsters_earning = tk.Label(game_platform0, text="Lobsters earning / sec:", height=2, font=("Courier", 15, "bold"), relief="solid", bg="#ab350c", fg="white")
lobsters_earning.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E, padx=5)

display_lobsters_earning = tk.Label(game_platform0, text="0$", font=("Courier", 15, "bold"), relief="ridge", bg="#ab350c", fg="white")
display_lobsters_earning.grid(row=1, column=2, sticky=tk.W + tk.E, padx=5)
#   }Game_Platform0


#   Game_Platform1{
#   New things{
#   }New things


#   Tap zone{
button_taptap = tk.Button(game_platform1, height=2, width=46, text="0$ / tap", font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
button_taptap.grid(row=0, columnspan=3, pady=10, padx=5)

name_taptap = tk.Label(game_platform1, text="Tap-tap Lobster: lvl 0", height=2, width=25, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
name_taptap.grid(row=1, column=0, sticky=tk.E + tk.W, padx=5)

upgrade_button_tap = tk.Button(game_platform1, state="disabled", text="Upgrade: 0$", height=1, width=15, font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
upgrade_button_tap.grid(row=1, column=1, sticky=tk.W + tk.E, padx=5)
#   }Tap zone


#   Auto tap{
unlock_autotap = tk.Button(game_platform1, height=3, text="Unlock Lobsters (0$)", state="disabled", font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
unlock_autotap.grid(row=2, columnspan=3, sticky=tk.W + tk.E, pady=10, padx=5)


Lobster_Bob = tk.Label(game_platform1, text="Lobster: ---", height=2, width=25, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
Lobster_Bob.grid(row=3, column=0, sticky=tk.E + tk.W, padx=5)

upgrade_Lobster_Bob = tk.Button(game_platform1, text="--------", state="disabled", height=1, width=15, font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
upgrade_Lobster_Bob.grid(row=3, column=1, sticky=tk.W + tk.E, padx=5)


Lobster_Doodle = tk.Label(game_platform1, text="Lobster: ---", height=2, width=25, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
Lobster_Doodle.grid(row=4, column=0, sticky=tk.E + tk.W, padx=5)

upgrade_Lobster_Doodle = tk.Button(game_platform1, text="--------", state="disabled", height=1, width=15, font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
upgrade_Lobster_Doodle.grid(row=4, column=1, sticky=tk.W + tk.E, padx=5)


Lobster_Winky = tk.Label(game_platform1, text="Lobster: ---", height=2, width=25, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
Lobster_Winky.grid(row=5, column=0, sticky=tk.E + tk.W, padx=5)

upgrade_Lobster_Winky = tk.Button(game_platform1, text="--------", state="disabled", height=1, width=15, font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
upgrade_Lobster_Winky.grid(row=5, column=1, sticky=tk.W + tk.E, padx=5)


Lobster_Fred = tk.Label(game_platform1, text="Lobster: ---", height=2, width=25, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
Lobster_Fred.grid(row=6, column=0, sticky=tk.E + tk.W, padx=5)

upgrade_Lobster_Fred = tk.Button(game_platform1, text="--------", state="disabled", height=1, width=15, font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
upgrade_Lobster_Fred.grid(row=6, column=1, sticky=tk.W + tk.E, padx=5)


Lobster_Giggles = tk.Label(game_platform1, text="Lobster: ---", height=2, width=25, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
Lobster_Giggles.grid(row=7, column=0, sticky=tk.E + tk.W, padx=5)

upgrade_Lobster_Giggles = tk.Button(game_platform1, text="--------", state="disabled", height=1, width=15, font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
upgrade_Lobster_Giggles.grid(row=7, column=1, sticky=tk.W + tk.E, padx=5)


Lobster_Larry = tk.Label(game_platform1, text="Lobster: ---", height=2, width=25, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
Lobster_Larry.grid(row=8, column=0, sticky=tk.E + tk.W, padx=5)

upgrade_Lobster_Larry = tk.Button(game_platform1, text="--------", state="disabled", height=1, width=15, font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
upgrade_Lobster_Larry.grid(row=8, column=1, sticky=tk.W + tk.E, padx=5)


Lobster_David_frame = tk.Frame(game_platform1, bg="black")
Lobster_David_frame.columnconfigure(0, weight=1)
Lobster_David_frame.grid(row=10, columnspan=3, pady=20)

Lobster_David = tk.Label(Lobster_David_frame, text="Secret Lobster...", height=2, width=25, font=("Courier", 15, "bold"), relief="solid", bg="#cc562d")
Lobster_David.grid(row=0, column=0, sticky=tk.E + tk.W, padx=5, pady=5)

upgrade_Lobster_David = tk.Button(Lobster_David_frame, text="--------", state="disabled", height=1, width=15, font=("Courier", 15, "bold"), bg="#ab350c", fg="White", activebackground="#ad2d00", activeforeground="white")
upgrade_Lobster_David.grid(row=0, column=1, sticky=tk.W + tk.E, padx=5, pady=5)
#   }Auto tap
#   }Game_Platform1


#   Game_Platform2{

#   }Game_Platform2



game.mainloop()
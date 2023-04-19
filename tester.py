from data.default_data import *

def taptap(a):
    global tap_lvl, tap_value, tap_upgrade_cost
    for x in range(a):
        print("taptap lvl:", tap_lvl)
        print("taptap value:", round(tap_value, 2))
        print("taptap upgrade cost:", round(tap_upgrade_cost, 2))
        print("tap upgrade cost / tap value", round(tap_upgrade_cost / tap_value, 2), "\n")
        tap_lvl += 1
        tap_value += tap_lvl * 0.5
        tap_upgrade_cost = tap_value * 5 + tap_lvl ** 2.6
    
def bob(a):
    global bob_lvl, bob_value, bob_upgrade_cost
    for x in range(a):
        print("bob lvl:", bob_lvl)
        print("bob value/sec:", round(bob_value, 2))
        print("bob upgrade cost:", round(bob_upgrade_cost, 2))
        print("earning / min:", round(bob_value * 60, 2))
        print("bob upgrade cost / bob value:", round((bob_upgrade_cost / bob_value) / 60, 2),"min\n")
        bob_lvl += 1
        bob_value = (bob_lvl / 2) ** 2
        bob_upgrade_cost = bob_value * 60 + bob_lvl ** 3.32

def doodle(a):
    global doodle_lvl, doodle_upgrade_cost, doodle_value
    for x in range(a):
        print("doodle lvl:", doodle_lvl)
        print("doodle value/sec:", round(doodle_value, 2))
        print("doodle upgrade cost:", round(doodle_upgrade_cost, 2))
        print("earning / min:", round(doodle_value * 60, 2))
        print("doodle upgrade cost / doodle value:", round((doodle_upgrade_cost / doodle_value) / 60, 2),"min\n")
        doodle_lvl += 1
        doodle_value = ((doodle_lvl / 2) ** 2) * 2.2
        doodle_upgrade_cost = doodle_value * 60 + doodle_lvl ** 3.581

def winky(a):
    global winky_lvl, winky_upgrade_cost, winky_value
    for x in range(a):
        print("winky lvl:", winky_lvl)
        print("winky value/sec:", round(winky_value, 2))
        print("winky upgrade cost:", round(winky_upgrade_cost, 2))
        print("earning / min:", round(winky_value * 60, 2))
        print("winky upgrade cost / winky value:", round((winky_upgrade_cost / winky_value) / 60, 2),"min\n")
        winky_lvl += 1
        winky_value = ((winky_lvl / 2) ** 2) * 3.6
        winky_upgrade_cost = winky_value * 60 + winky_lvl ** 3.752

def fred(a):
    global fred_lvl, fred_upgrade_cost, fred_value
    for x in range(a):
        print("fred lvl:", fred_lvl)
        print("fred value/sec:", round(fred_value, 2))
        print("fred upgrade cost:", round(fred_upgrade_cost, 2))
        print("earning / min:", round(fred_value * 60, 2))
        print("fred upgrade cost / fred value:", round((fred_upgrade_cost / fred_value) / 60, 2),"min\n")
        fred_lvl += 1
        fred_value = ((fred_lvl / 2) ** 2) * 5.2
        fred_upgrade_cost = fred_value * 60 + fred_lvl ** 3.881

def giggles(a):
    global giggles_lvl, giggles_upgrade_cost, giggles_value
    for x in range(a):
        print("giggles lvl:", giggles_lvl)
        print("giggles value/sec:", round(giggles_value, 2))
        print("giggles upgrade cost:", round(giggles_upgrade_cost, 2))
        print("earning / min:", round(giggles_value * 60, 2))
        print("giggles upgrade cost / giggles value:", round((giggles_upgrade_cost / giggles_value) / 60, 2),"min\n")
        giggles_lvl += 1
        giggles_value = ((giggles_lvl / 2) ** 2) * 7
        giggles_upgrade_cost = giggles_value * 60 + giggles_lvl ** 4.009

def larry(a):
    global larry_lvl, larry_upgrade_cost, larry_value
    for x in range(a):
        print("larry lvl:", larry_lvl)
        print("larry value/sec:", round(larry_value, 2))
        print("larry upgrade cost:", round(larry_upgrade_cost, 2))
        print("earning / min:", round(larry_value * 60, 2))
        print("larry upgrade cost / larry value:", round((larry_upgrade_cost / larry_value) / 60, 2),"min\n")
        larry_lvl += 1
        larry_value = ((larry_lvl / 2) ** 2) * 9
        larry_upgrade_cost = larry_value * 60 + larry_lvl ** 4.094

larry(1000)

"""
value on lvl 1000

bob = 250 K (+300)
doodle = 550 K (+350)
winky = 900 K (+400)
fred = 1.300 M (+450)
giggles = 1.750 M (+500)
larry = 2.250 M
"""
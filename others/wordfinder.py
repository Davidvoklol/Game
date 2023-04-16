b = input("word:\t")
print("")
c = 0
with open("Idle Lobster.py", "r") as f:
    a = f.readlines()
    for x in a:
        if b in x:
            print("Sor szám:", a.index(x) + 1, "-->", a[a.index(x)])
            c += 1
if c == 0:
    print("Not found")
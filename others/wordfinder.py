b = input("word:\t")
print("")
number = []
c = 0
with open("Idle Lobster.py", "r") as f:
    a = f.readlines()
    for x in range(len(a)):
        if b in a[x]:
            print("Sorszám:", x + 1, "-->", a[x])
            c += 1
if c == 0:
    print("Not found")
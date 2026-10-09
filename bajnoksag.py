eredmeny = input("Eredménysorozat: ")

gyozelem = 0
dontetlen = 0
vereseg = 0
for betu in eredmeny:
    if betu == "G":
        gyozelem = gyozelem + 1
    elif betu == "D":
        dontetlen = dontetlen + 1
    elif betu == "V":
        vereseg = vereseg + 1
print(f"Győzelem:{gyozelem}. Döntetlen:{dontetlen}. Vereség:{vereseg}.")

pont = gyozelem * 3 + dontetlen * 1
print(f"A csapat {pont} pontot szerzett.")

if vereseg == 0:
    print("Nem volt vereég.")
else:
    print("Vereség volt.")
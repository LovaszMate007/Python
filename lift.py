utasok = [72, 85, 64, 91, 58, 103, 77, 69, 88, 95, 60, 81]

teher = int(input("A lift teherbírása (kg): "))

osszes = 0
for tomeg in utasok:
    osszes = osszes + tomeg
if osszes <= teher:
    print(f"Az összes tömeg {osszes} kg. Mindenki befér.")
else:
    print(f"Az összes tömeg {osszes} kg. Nem fér be mindenki.")

nehez_utas = -1
i = 0
while i < len(utasok) and nehez_utas == -1:
    if utasok[i] > 100:
        nehez_utas = i
    i = i + 1
if nehez_utas != -1:
    print(f"A 100 kg feletti utas: {nehez_utas + 1}. ({utasok[nehez_utas]} kg)")
else:
    print(" Nincs 100 kg feletti utas.")
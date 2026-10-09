lepesekszama = [6500, 8200, 4300, 10100, 7600, 12000, 5400, 9800, 3900, 11200]

osszes = 0

for lepes in lepesekszama:
    osszes = osszes + lepes

atlag = osszes / len(lepesekszama)
print(f"Összesen {osszes} lépés átlag: {atlag}")

legtobb = lepesekszama[0]
nap = 1
for i in range(1, len(lepesekszama)):
    if lepesekszama[i] > legtobb:
        legtobb = lepesekszama[i]
        nap = i + 1
print(f"A legtöbb lépés: {legtobb} a {nap} napon volt.")

napok = 0
for lepes in lepesekszama:
    if lepes >= 10000:
        napok = napok + 1
print(f"{napok} napon volt minumim 10000 lépés.")
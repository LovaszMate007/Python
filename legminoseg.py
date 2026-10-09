meresek = [42, 55, -1, 61, 48, -1, 70, 66]

darab = 0
osszes = 0
for meres in meresek:
    if meres != -1:
        darab = darab + 1
        osszes = osszes + meres
atlag = osszes / darab
print(f"Érvényes mérések száma: {darab}. Átlaga: {atlag}")

szoveg = []
for ora in range(len(meresek) // 2):
    ora_ossz = 0
    for index in (2 * ora, 2 * ora + 1):
        if meresek[index] != -1:
            ora_ossz = ora_ossz + meresek[index]
    szoveg.append(f"{8 + ora} órától {ora_ossz}")
print("Érvényes mérések óránként: " + ", ".join(szoveg))

legnagyobb = meresek[0]
legnagyobbak = 0
for i in range(1, len(meresek)):
    if meresek[i] > legnagyobb:
        legnagyobb = meresek[i]
        legnagyobbak = i
percek = legnagyobbak * 30
ora = 8 + percek // 60
perc = percek % 60
print(f"A legnagyobb érték: {legnagyobb}. Ideje: {ora}:{perc:02d}")
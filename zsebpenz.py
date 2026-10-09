koltes = [1200, 800, 1500, 700, 900, 1100, 400]

egyenleg = 5000
elmarad = 0
elso_elmaradas = 0
napi = []
for i in range(len(koltes)):
    if koltes[i] <= egyenleg:
        egyenleg = egyenleg - koltes[i]
    else:
        elmarad = elmarad + 1
        if elso_elmaradas == 0:
            elso_elmaradas = i + 1
    napi.append(str(egyenleg))
print("Maradék" + " ".join(napi))

if elmarad > 0:
    print(f"{elmarad} napon maradt el a vásárlás. Legelőször az {elso_elmaradas}-dik napon.")
else:
    print("Minden nap sikerült vásárolni.")

if egyenleg >= 500:
    print("Maradt tartalék.")
else:
    print("Nem maradt tartalék.")
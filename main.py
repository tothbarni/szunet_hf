import metodusok
#1
szam:int = int(input("Írj be egy számot 200 és 920 között : "))
if (szam >= 200) and (szam <= 920):
    elso:int = str(szam)[0]
    print(f"A szám első számjegye: {elso}")
else:
    print("Hiba! Nem a feltételnek megfelelő számot adtál meg!")

#2
oraszam:int = int(input("Óraszám: "))
metodusok.munkabiras(oraszam)

#4
szam = float(input("Adj meg egy valós számot: "))
if szam < 0:
    print("Hiba: Negatív számból nem lehet négyzetgyököt vonni!")
else:
    gyok = szam ** 0.5
    print(f"A szám négyzetgyöke: {gyok:.4f}")

#9
metodusok.szorzotabla()

#12
szam = int(input("Adj meg egy pozitív egész számot: "))
oszto_osszeg = metodusok.feladat12(szam)
metodusok.feladat12_kiir(szam, oszto_osszeg)
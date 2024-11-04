def munkabiras(ora):
    if ora < 1:
        print("Be se jövök!")
    elif ora == 1:
        print("Még 90% on vagyunk!")
    elif 2 <= ora <= 3:
        print("Még bírjuk (60%)")
    elif 4 <= ora <= 7:
        print("Progit tanulunk, töltődünk! 70%")
    elif 8 <= ora <= 9:
        print("Lassan nem bírjuk tovább! 50%")
    else:
        print("Ez már tényleg túlzás.")

def szorzotabla():
    print("A 10x10-es szorzótábla:")
    for i in range(1, 11, 1): 
        for j in range(1, 11, 1):
            print(f"{i * j:4}", end=" ") 
        print()

def feladat12(szam: int) -> int:
    osztok = []
    for i in range(1, szam):
        if szam % i == 0:
            osztok.append(i)
    oszto_osszeg: int = sum(osztok)
    return oszto_osszeg

def feladat12_kiir(szam: int, oszto_osszeg: int):
    if oszto_osszeg == szam:
        print(f"A(z) {szam} tökéletes szám!")
    else:
        print(f"A(z) {szam} nem tökéletes szám!")
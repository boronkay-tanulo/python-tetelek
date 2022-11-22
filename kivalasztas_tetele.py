def eldontes(ertek, sorozat):
    for e in sorozat:
        if e == ertek:
            return True
    return False

# Míg az eldöntés tételénél az volt a feltételünk, hogy van egy sorozatunk, meg egy elemünk, itt már az is feltétel, hogy az elem legalább
# legalább egyszer szerepel a sorozatban. Magyarul: az eldöntés tétele egy "True" értéket adott vissza. A kiválasztás tétele csakis az
# eldöntés tételével együtt értelmezhető! A kiválasztás tétele egyetlen értéket küldhet vissza, eé ez az elem első előfordulásának
# az indexe a sorozatban.

def kivalasztas(elem, sorozat):
    for i in range(len(sorozat)): # az "i" a sorozat indexeit hozza
        if elem == sorozat[i]:
            return i

# FŐPROGRAM
# Létrehozzuk a sorozatot, beolvassuk a keresett elemet. Meghívjuk az eldöntés tételét, ha igazat ad vissza, akkor meghívjuk
# a kiválasztás tételét.
sorozat = [4,34,8,5,98,234,5,6,98,32]
elem = int(input("Mit keresünk? "))
if eldontes(elem, sorozat):
    print(f"A keresett elem a sorozat {kivalasztas(elem, sorozat)} indexű tagja")
else:
    print("A keresett elem nincs a sorozatban.")
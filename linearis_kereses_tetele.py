# Gyakorlatilag egybevesszük az eldöntés és kiválasztás tételét. Két megközelítése van a tételnek: Az egyik. hogyha a függvény -1-et
# ad vissza, akkor nincs a sorozatban az elem. -1-es index nincs, ebből tudja a hívó fél, hogy eredménytelen a a keresés.
# A másik, hogyha a függvény az elemszámot adja vissza (ez a hivatalos verzió) indexként, akkor tudjuk, hogy egy "n" elemű sorozatban
# a legnagyobb index "n-1".
# Találat esetén 0 <= index < n eredményt kapunk.
# FONTOS! Megírhatjuk úgy is, hogy az UTOLSÓ előfordulást adja vissza a függvény, de alapértelmezetten az ELSŐ előfordulás indexét kapjuk!
# Hivatalos verzió, az első elem előfordulása.
def linkeres(elem, sorozat):
    index = 0
    while index < len(sorozat) and elem != sorozat[index]:
        index += 1
    return index

# FŐPROGRAM:
sorozat = [2,5,7,4,98,23,4,76,89,55,2,65,454,1,120]
elem = int(input("Mit keresünk? "))
index = linkeres(elem, sorozat)
if index == len(sorozat):
    print("Ez az elem nincs a sorozatban!")
else:
    print(f"A(z) {elem} a sorozat {index} indexű eleme.")
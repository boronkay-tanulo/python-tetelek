# Eldöntés tétele: Ha egy elem benne van egy sorozatban, akkor IGAZ a visszatérési érték, különben HAMIS.
# Az dönti el, hogy szerepel-e a sorozatban.
# A függvény két paramétert kap: az egyik az elem, a másik a sorozat.
def eldontes(ertek, sorozat): # formális paraméterlista
    for e in sorozat:
        if e == ertek:
            return True
    return False # ez akkor fog bekövetkezni, ha kiléptem a ciklusból.
    # A ciklusból cska akkor léphetek ki, ha nem találom benne az "ertek" változó által hordozott értéket.

# FŐPROGRAM
# létrehozom a sorozatot, ami most egy lista
sorozat = ["anyu", "apu", "Józsika", "Bodri", "Cirmi", "Gedeon az aranyhal"]
elem = input("Mit keresünk? ")
if eldontes(elem, sorozat):
    print("Benne van")
else:
    print("Nincs benne")

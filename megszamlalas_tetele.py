# Van egy elemünk és egy sorozatunk. Hányszor szerepel az elem a sorozatban?
def megszamlalas(elem, sorozat):
    szamlalo = 0 # Feltételezzük. hogy nem is szerepel benne.
    for e in sorozat:
        if e == elem:
            szamlalo += 1
    return szamlalo

# FŐPROGRAM: sorozatot készítek, elemet olvasok be:
sorozat = [10,20,10,33,69,420,10,20,20,11,11,10]
elem = int(input("Adj meg egy számot! "))
print(f"A {elem} a sorozatban {megszamlalas(elem, sorozat)} alkalommal foldul elő.")
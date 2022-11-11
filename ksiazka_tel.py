tel = {}



def dodaj_numer(imie,nazwisko,typ,numer):
    if (imie,nazwisko) in tel:
        tel[(imie,nazwisko)]=[(typ,numer)]
    else:
        tel[(imie,nazwisko)].append((typ,numer))


dodaj_numer("Jan","Kowalski", "praca", "123-456-789")
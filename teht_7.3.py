lentoasemat = {}

while True:
    valinta = input("Haluatko syöttää uuden lentoaseman, hakea lentoaseman vai lopettaa? ")

    if valinta == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")

        lentoasemat[icao] = nimi

    elif valinta == "haku":
        icao = input("Anna ICAO-koodi: ")

        if icao in lentoasemat:
            print(lentoasemat[icao])

    elif valinta == "lopeta":
        break
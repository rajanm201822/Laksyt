oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    annettu_salasana = input("Salasana: ")

    if tunnus == oikea_tunnus and annettu_salasana == oikea_salasana:
        print("Tervetuloa")
        break

    yritykset = yritykset + 1

if yritykset == 5:
    print("Pääsy evätty")
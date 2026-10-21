
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nykyinen_nopeus += nopeuden_muutos

        if self.nykyinen_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus

        if self.nykyinen_nopeus < 0:
            self.nykyinen_nopeus = 0



auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print(auto1.nykyinen_nopeus)

auto1.kiihdytä(-200)

print(auto1.nykyinen_nopeus)



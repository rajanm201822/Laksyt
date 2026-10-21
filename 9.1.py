
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0


auto1 = Auto("ABC-123", 142)

print(auto1.rekisteritunnus)
print(auto1.huippunopeus)
print(auto1.nykyinen_nopeus)
print(auto1.kuljettu_matka)

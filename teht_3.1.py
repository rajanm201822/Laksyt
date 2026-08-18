# Ohjelma kysyy kuhan pituuden. Jos kuha on alle 37 cm,
# ohjelma kertoo, että se pitää laskea takaisin järveen ja ilmoittaa,
# kuinka monta senttiä pituudesta puuttuu.

pituus = int(input("mikä on kuhan pituus?"))

if pituus < 37:
    alamittaisuus = 37 - pituus

    print(f"Kalasi on {alamittaisuus} cm liian lyhyt!")
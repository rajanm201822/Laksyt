#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
# (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan
# luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
#Jos käyttäjä syöttää kelvottoman hyttiluokan,
# ohjelma tulostaa Virheellinen hyttiluokka.



hytti = input("Anna hyttiluokka: ")

if hytti == "LUX":
    print("parvekkeellinen hytti yläkannella.")

elif hytti == "A":
    print("ikkunallinen hytti autokannen yläpuolella")

elif hytti == "B":
    print("ikkunaton hytti autokannen yläpuolella.")

else:
    print("virheellinen hyttiluokka")


def gallona_litroiksi(gallona):
    return gallona * 3.785


while True:
    gallonat = float(input("Anna gallonamäärä: "))

    if gallonat < 0:
        break

    litrat = gallona_litroiksi(gallonat)
    print(f"Litroina: {litrat}")
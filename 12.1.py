import requests

URL = "https://api.chucknorris.io/jokes/random"


def hae_vitsi():
    vastaus = requests.get(URL, timeout=10)
    vastaus.raise_for_status()
    return vastaus.json()["value"]


try:
    print(hae_vitsi())
except requests.exceptions.RequestException:
    print("Vitsin hakeminen epäonnistui. Tarkista verkkoyhteys ja yritä uudelleen.")
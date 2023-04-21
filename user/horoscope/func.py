from bs4 import BeautifulSoup
import requests


def return_horoscope(data="taurus"):

    URL=f"https://astrohelper.ru/horoscope/{data}/"
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, "html.parser")


    horoscop_text = soup.find("div", class_="mt-3").find("p").text
    return horoscop_text




from bs4 import BeautifulSoup
import requests


def return_vostok(data="ox"):
    
    URL = f"https://astrohelper.ru/east-horoscope/{data}/"
    request = requests.get(URL)

    soup = BeautifulSoup(request.text, "html.parser")

    horoscop_text = soup.find("div", class_="col-md-8 col-sm-12").find("div",class_="mt-3").text
    return horoscop_text

    





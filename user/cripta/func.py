from bs4 import BeautifulSoup
import requests


def return_cripta():
    
    URL = f"https://coinmarketcap.com/ru/"
    request = requests.get(URL)

    soup = BeautifulSoup(request.text, "html.parser")

    BTC = soup.find("div", class_="sc-1a736df3-0 PimrZ cmc-body-wrapper").find("div",class_="sc-beb003d5-2 bkNrIb").find("tbody").find("td",style="text-align:end").text[1:]
    ETH = soup.find("div", class_="sc-1a736df3-0 PimrZ cmc-body-wrapper").find("div",class_="sc-beb003d5-2 bkNrIb").find("tbody").find("tr").find_next_sibling().find("td",style="text-align:end").text[1:]
    USDT = soup.find("div", class_="sc-1a736df3-0 PimrZ cmc-body-wrapper").find("div",class_="sc-beb003d5-2 bkNrIb").find("tbody").find("tr").find_next_sibling().find_next_sibling().find("td",style="text-align:end").text[1:]
    BND = soup.find("div", class_="sc-1a736df3-0 PimrZ cmc-body-wrapper").find("div",class_="sc-beb003d5-2 bkNrIb").find("tbody").find("tr").find_next_sibling().find_next_sibling().find_next_sibling().find("td",style="text-align:end").text[1:]
    USDC = soup.find("div", class_="sc-1a736df3-0 PimrZ cmc-body-wrapper").find("div",class_="sc-beb003d5-2 bkNrIb").find("tbody").find("tr").find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find("td",style="text-align:end").text[1:]
    
    cripto_dict = {
"BTC" : BTC,
"ETH" : ETH,
"USDT" : USDT,
"BND" : BND,
"USDC" : USDC
    }
    return cripto_dict


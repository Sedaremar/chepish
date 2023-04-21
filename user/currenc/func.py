from bs4 import BeautifulSoup
import requests





def return_currenc():
    USD="https://www.x-rates.com/table/?from=USD&amount=1"
    EUR="https://www.x-rates.com/table/?from=EUR&amount=1"
    KZT="https://www.x-rates.com/table/?from=KZT&amount=1"
    requestUSD = requests.get(USD)
    requestEUR = requests.get(EUR)
    requestKZT = requests.get(KZT)
    soupUSD = BeautifulSoup(requestUSD.text, "html.parser")
    soupEUR = BeautifulSoup(requestEUR.text, "html.parser")
    soupKZT = BeautifulSoup(requestKZT.text, "html.parser")


    dolar = soupUSD.find("table", class_="tablesorter ratesTable").find("a", href="https://www.x-rates.com/graph/?from=USD&to=RUB").text
    euro = soupEUR.find("table", class_="tablesorter ratesTable").find("a",href="https://www.x-rates.com/graph/?from=EUR&to=RUB").text
    tenge = soupKZT.find("table", class_="tablesorter ratesTable").find("a",href="https://www.x-rates.com/graph/?from=KZT&to=RUB").text



    dolar = "%.2f" % float(dolar)
    euro = "%.2f" % float(euro)
    tenge = "%.2f" % float(tenge)

    currenc_dict ={
    
"USD" : dolar,
"EUR" : euro,
"KZT" : tenge
}

    return currenc_dict

# 21


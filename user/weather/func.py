
from bs4 import BeautifulSoup
import requests





def return_weather(city="Moscow"):
    
    URL = f"https://weather.rambler.ru/{city}/today/"
    request = requests.get(URL)

    soup = BeautifulSoup(request.text, "html.parser")

    location = soup.find("div", class_="n9l9").text

    #НОЧЬ УТРО ДЕНЬ ВЕЧЕР
    degree = soup.find("div", class_="qRFP").find("div",class_="ALjB").find_all("span",class_="Njqa")
    night = degree[0].text
    morn = degree[1].text
    day = degree[2].text
    even = degree[3].text
    
    
    specif = soup.find("div", class_="qRFP").find("div",class_="xNuK CGpf ioix").find_all("div")
    wind = specif[0].text
    presur = specif[1].text 
    sunr1 = specif[2].text[:12]
    sunr2 = specif[2].text[12:]
    sunr=sunr1+ ' ' +sunr2
    day_hour = specif[3].text 
    
    weather_dict = {
"degree" :{
"night" : night,
"morn" : morn,
"day" : day,
"even" : even
},
"spec" : {
"wind" : wind,
"presur" : presur,
"sunr" : sunr,
"day_hour" : day_hour,
"loc" : location

        }
                    }
    
    return weather_dict



    
    
# print(return_weather())
# 141
    


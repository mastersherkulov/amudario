from bs4 import BeautifulSoup
import requests

def get_aqiwgtvalue():
    url_page = "https://aqicn.org/city/uzbekistan/tashkent/us-embassy/"
    _html = requests.get(url_page).content
    aqiwgtvalue = BeautifulSoup(_html, features="html.parser")
    return aqiwgtvalue.find("div", {"id": "aqiwgtvalue"}).text
import requests
from bs4 import BeautifulSoup as bs

html = requests.get("https://xn--80aesfpebagmfblc0a.xn--p1ai/information/")
soup = bs(html.text, "html.parser")
item = soup.find_all("cv-stats-virus")
date = (str(item[0]).split(" :")[1]).split("'")[1].split('"')[3]
stats = eval((str(item[0]).split(" :")[2]).split("'")[1])
print("На момент даты", date, "в России:", end="\n\n")
print("За всё время заболело коронавируcом -", stats["sick"])
print("За день заболело -", stats["sickChange"][1::])
print("За день выздоровело -", stats["healedChange"][1::])
print("За день умерло -", stats["diedChange"][1::], end="\n\n")
print("За всё время выздоровело -", stats["healed"])
print("За всё время умерло -", stats["died"])

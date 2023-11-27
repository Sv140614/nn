import requests
from bs4 import BeautifulSoup
import pandas as pd
headers={"User-Agent":"User-Agent ittensive-python-scraper/1.0 (+https://ittensive.com)"}
r=requests.get("https://market.yandex.ru/catalog--kholodilniki-saratov/71639/list?hid=15450081&rs=eJwzamIOYDzKyLAg0xZEzrIGkgwvbUAk-x4g2XDNCsSeCBJpYAWRDnN3g1TmgVUeAYtMAJEPVEHqGXJAsg6PwSLbwOwdIPYCbbDsdJCIwnUQe0EIiHQIAdurAVbTD5JNOAtm7wW7gWEnSIQBpIZhPUjkwBOQvQeq94PM8QTJKtiAxBMiwLo2gsx84A1Sn_AZLMINYju0gG1xAcsygdnGILsYJoBMe1AL9t0fEKlwAUweA8k-mAUW7wKFwIOVYNtvgGXvgnQteAa2VwVsi-JekKwF2M0sIPMP8ILZi8GyImDyGcj2hAYw2wscGpfA_tW0BgCnsIZY&allowCollapsing=1&local-offers-first=0&glfilter=7893318%3A152776", headers=headers)
html=BeautifulSoup(r.content)
title=html.find_all("a", {"class":"grid-snippet__react-link"})
for link in title:
    if str(title).find("Саратов 263") > -1:
        link_263=link["href"]
    if str(title).find("Саратов 452") > -1:
        link_452 = link["href"]
def find_volume (link):
    r = requests.get("https://beru.ru" + link_263)
    html = BeautifulSoup(r.content)
    volume = html.find_all("span", {"class": "_112Tad-7AP"})
    return int(''.join(i for in volume[2].get_text() if i.istigit()))


if link_263 and link_452:
    volume_263=find_volume (link_263)
    volume_452 = find_volume(link_452)
    diff=max(volume_263, volume_452)-min(volume_263, volume_452)
    print(diff)

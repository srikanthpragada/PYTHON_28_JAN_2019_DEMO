import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text, "xml")  # text, parser

for item in bs.find_all("item"):
    print(item.title)
    print(item.link)

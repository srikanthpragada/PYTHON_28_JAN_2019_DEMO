
import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text, "html.parser")

for a in bs.find_all("a"):
    if 'href' not in a.attrs:
        continue

    if a['href'] != '#':
        print(a['href'])




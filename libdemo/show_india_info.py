# Program to display information about India
import requests
import sys

code = input("Enter 2 letter country code : ")
resp = requests.get("https://restcountries.eu/rest/v2/alpha/" + code)
if resp.status_code != 200:
    print("Sorry! Could not find country code!")
    sys.exit(1)

# convert json to  dict
info = resp.json()

for (name, value) in info.items():
    print(f"{name:20s} - {value}")

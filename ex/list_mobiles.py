import re

f = open("mobile.txt")

for line in f.readlines():
    mobiles = re.findall(r"\d+",line)
    for m in mobiles:
        if len(m) == 10:
            print(m)

f.close()
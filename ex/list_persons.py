from datetime import datetime, timedelta
import math


def get_age(dob):
    today = datetime.today()
    days = (today - dob).days
    years = days // 365
    months = (days % 365) // 30
    days = days - (years * 365 + months * 30)
    return (years, months, days)


print(get_age(datetime(year=2000, month=10, day=1)))

f = open("persons.txt")
persons = {}
today = datetime.today()

for line in f.readlines():
    # remove \n at the end of line
    line = line.strip("\n")
    parts = line.split(",")
    name = parts[0]
    try:
        dob = datetime.strptime(parts[1], "%d/%m/%Y")
        age_years = math.trunc((today - dob).days / 365)
        persons[name] = age_years
    except:
        pass

f.close()

# Sort dict by values
for (name, age) in sorted(persons.items(), key=lambda t: t[1]):
    print(f"{name:20s} {age}")

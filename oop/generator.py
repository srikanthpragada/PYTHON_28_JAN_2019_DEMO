def numbers():
    for n in range(1, 11):
        yield n


for n in numbers():
    print(n)

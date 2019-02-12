def change(n):
    print(id(n))
    n = 0
    print(id(n))

v = 100
print(id(v))
change(v)
print(v)

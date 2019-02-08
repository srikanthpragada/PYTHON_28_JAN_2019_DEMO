def add(n1, n2):
    return n1 + n2


def mul(n1, n2=10):
    return n1 * n2


def divide(n1=100, n2=2):
    return n1 / n2


total = add(10, 20)
print(total)
print(mul(10, 20))
print(mul(11))

print(divide(n2=5, n1=25))
print(divide(n2=15))


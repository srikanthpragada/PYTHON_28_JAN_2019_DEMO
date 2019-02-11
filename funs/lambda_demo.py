def process(n1, n2, op):
    print(op(n1, n2))


def add(a, b):
    return a + b


fsub = lambda x, y: x - y

print(fsub(10, 5))

process(10, 20, add)
process(10, 20, lambda x, y: x * y)
process(10, 20, lambda x, y: x / y)

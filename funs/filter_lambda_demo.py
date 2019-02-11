l = [10, 11, 14, 55, 20]

# method 1
# for n in l:
#     if n % 2 == 0:
#         print(n)


def iseven(n):
    return n % 2 == 0


# Method 2
# en = filter(iseven, l)
en = filter(lambda v: v % 2 != 0, l)
for n in en:
    print(n)

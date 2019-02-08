
def add(*nums, format=""):
    total = 0
    for n in nums:
        total += n

    return total


print( add(10,20,30,20))
print( add(10,20, format="abc") )
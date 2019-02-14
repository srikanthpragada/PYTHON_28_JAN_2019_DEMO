# Program to display common factors for numbers given on command line
import sys

nums = []
for v in sys.argv[1:]:
    nums.append(int(v))

min_num = min(nums)

factors = []
for i in range(2, min_num // 2 + 1):
    for v in nums:
        if v % i != 0:
            break
    else:
        factors.append(i)

# print common factors
if len(factors) == 0:
    print("Sorry! No common factors found!")
else:
    for n in factors:
        print(n)


# Print factors of the given number
import sys

print(sys.argv)

num = int(sys.argv[1])
for i in range(2, num//2+1):
    if num % i == 0:
        print(i)
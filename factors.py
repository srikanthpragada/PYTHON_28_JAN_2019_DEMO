# Print factors of the given number
import sys

if len(sys.argv) < 2:
    print("Missing number!")
    sys.exit(0)

num = int(sys.argv[1])
for i in range(2, num//2+1):
    if num % i == 0:
        print(i)
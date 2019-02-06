# Take numbers from user and put positive numbers on left
# negative numbers on right

pos = []
neg = []

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num > 0:
        pos.append(num)
    else:
        neg.append(num)

for n in pos + neg:
    print(n)

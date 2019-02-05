# Take numbers from user and put positive numbers on left
# negative numbers on right
nums = []

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num > 0:
        nums.insert(0,num)
    else:
        nums.append(num)

for n in nums:
    print(n)

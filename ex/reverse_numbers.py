# Take numbers from user and put only unique value into list and
# print it in reverse order
nums = []

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    if num not in nums:
        nums.append(num)

for n in reversed(nums):
    print(n)

total = 0
i = 1
while i <= 5:
    try:
        num = int(input("Enter a number :"))
        total += num
        i += 1
    except ValueError as ex:
        print("Sorry! Invalid number.", ex)
    except:
        print("Sorry! Unknown error. ")

print(total)

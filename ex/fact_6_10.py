for n in range(11, 21):
    fact = 1

    for i in range(2, n + 1):
        fact *= i

    print(f"{n:2d} - {fact}")

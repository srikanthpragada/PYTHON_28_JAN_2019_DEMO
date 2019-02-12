v1 = 10


def fun1():
    v2 = 20
    global v1
    v1 = 11

    # Local function
    def fun2():
        v3 = 30
        nonlocal v2  # refer to enclosing variable
        v2 = 21
        print(v3,v2, v1, True)

    # back in fun1
    fun2()
    print(v1, v2)


print(v1)
fun1()

class A:
    def process(self):
        print("Processing A")


class B(A):
    def process(self):
        print("Processing B")


class C(A, B):
    pass


obj = C()
print(C.__mro__)

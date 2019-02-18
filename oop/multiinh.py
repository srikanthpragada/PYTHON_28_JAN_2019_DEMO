class A:
    def read(self):
        print("Reading in A")

    def process(self):
        print("Processing A")


class B:
    def process(self):
        print("Processing B")


class C(B,A):
    def task(self):
        print("Task in C")


obj = C()
print( C.__mro__)


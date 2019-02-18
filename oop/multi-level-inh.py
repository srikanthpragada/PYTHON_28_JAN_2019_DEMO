class A:
    def read(self):
        print("Reading in A")

    def process(self):
        print("Processing A")


class B(A):
    def process(self):
        print("Processing B")


class C(B):
    def process(self):
        print("Processing C")


obj = C()
obj.process()
obj.read()
obj.__str__()

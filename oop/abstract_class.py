from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def get_occupation(self):
        pass


class Student(Person):
    def __init__(self, name):
        self.name = name

    @property
    def fullname(self):
        # Process
        return self.name

    @fullname.setter
    def fullname(self,name):
        self.name = name

    def get_occupation(self):
        return "Student"


# p = Person()
s = Student("Abc")
s.fullname = "BBC"
print(s.fullname)

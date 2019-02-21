# Iterator demo

class Months_Iterator:
    def __init__(self, months):
        self.pos = 0
        self.months = months

    def __next__(self):
        if self.pos == len(self.months):
            raise StopIteration
        else:
            p = self.pos
            self.pos += 1
            return self.months[p]


class Months:
    names = ["Jan", "Feb", "Mar"]

    def __iter__(self):
        return Months_Iterator(Months.names)

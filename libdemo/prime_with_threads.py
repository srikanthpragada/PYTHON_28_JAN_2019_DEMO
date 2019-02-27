from threading import Thread


class PrimeThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        for n in range(2, self.num // 2 + 1):
            if self.num % n == 0:
                print(f"{self.num} is not a prime number!")
                break
        else:
            print(f"{self.num} is a prime number!")


nums = [393939393, 10271, 383881818181123, 24]
for n in nums:
    t = PrimeThread(n)
    t.start()

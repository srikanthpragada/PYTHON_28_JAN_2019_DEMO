from threading import Thread
import threading


def print_nums():
    for i in range(1, 11):
        print("Child ", i)


print(threading.current_thread())

t = Thread(target=print_nums)
t.start()

for i in range(1, 11):
    print("Main ", i)

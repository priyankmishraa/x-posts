"""
What will be the output?

1. 0 1 2 3 4 5 6 7 8 9
2. 1 0 3 2 5 4 7 6 9 8
3. 0 2 4 6 8 1 3 5 7 9
4. 1 3 5 7 9 0 2 4 6 8

"""
import threading

def print_even():
    for i in range(0, 10, 2):
        print(i)

def print_odd():
    for i in range(1, 10, 2):
        print(i)

thread1 = threading.Thread(target=print_even)
thread2 = threading.Thread(target=print_odd)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

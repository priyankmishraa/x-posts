"""
What will be the output?

1. 0 1 2 3 4
2. 0 1 2 3 4 5
3. 4 3 2 1 0
4. 0 2 4 6 8

"""
import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()

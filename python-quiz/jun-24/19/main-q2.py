"""
What will be the output?

1. 1 4 9 16
2. 1 8 27 64
3. 1 9 27 64
4. 1 4 27 64

"""
import multiprocessing

def cube_numbers(numbers):
    for n in numbers:
        print(n**3)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    process = multiprocessing.Process(target=cube_numbers, args=(numbers,))
    process.start()
    process.join()

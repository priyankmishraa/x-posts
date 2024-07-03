"""
What will be the output?

1. 0 1 2 3 4 5 6
2. 0 2 4 6
3. 1 3 5 7
4. 0 2 4

"""
def even_numbers_up_to(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

evens = even_numbers_up_to(7)
for num in evens:
    print(num)

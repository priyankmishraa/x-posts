"""
What will be the output?

1. 1 3 5
2. 1 3 5 Done
3. 1 3 Done
4. 1 3 5 Done Done Done

"""
data = [1, 3, 5]
iterator = iter(data)
for _ in range(3):
    try:
        print(next(iterator))
    except StopIteration:
        print("Done")

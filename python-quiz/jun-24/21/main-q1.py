"""
What will be the output?

1. 1 2 3
2. 1 2 3 4 Loop completed
3. 1 2 3 4
4. 1 2 3 Loop completed

"""
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 4:
        break
    print(num)
else:
    print("Loop completed")

"""
What will be the output?

1. 1 2 3 Loop completed without break.
2. 1 2 Loop completed without break.
3. 1 2 
4. Loop completed without break.
"""

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)
else:
    print("Loop completed without break.")

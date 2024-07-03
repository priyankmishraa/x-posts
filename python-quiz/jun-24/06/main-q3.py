"""
What will be the output?

1. 0 1 2
2. 0 1 4
3. 1 4 9
4. 0 1 4 9

"""
def generate_squares(n):
    for i in range(n):
        yield i**2

squares = generate_squares(3)
for square in squares:
    print(square)

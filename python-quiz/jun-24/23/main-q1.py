"""
What will be the output?

1. one
2. one three
3. Two
4. three

"""
tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
for number, word in tuples:
    if number % 2 == 0:
        continue
    print(word)

"""
What will be the output?

1. one two
2. One
3. one two three
4. two three

"""

tuples = [(1, 'one'), (2, 'two'), (3, 'three')]
for number, word in tuples:
    if number > 2:
        break
    print(word)

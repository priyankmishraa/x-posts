"""
What will be the output in the file?

1. Line 1 Line 2 Line 3
2. Line 0 Line 1 Line 2
3. Line 0 Line 1 Line 2 Line 3
4. Line 1 Line 2 Line 3 Line 4

"""

with open('test.txt', 'w') as f:
    for i in range(3):
        f.write(f'Line {i}\n')

with open('test.txt', 'r') as f:
    print(f.read())

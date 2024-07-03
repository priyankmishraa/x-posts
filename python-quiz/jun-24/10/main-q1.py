"""
What will be the output in the file?

1. 1 2 3
2. 0 1 2
3. 1 2 3 4
4. 0 1 2 3

"""
with open('test.txt', 'w') as f:
    for i in range(3):
        f.write(str(i))

with open('test.txt', 'r') as f:
    print(f.read())

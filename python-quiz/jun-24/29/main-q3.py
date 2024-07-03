"""
What will be the output in the file?

1. 0 1 2
2. 0 1 2 3
3. 1 2 3
4. 0 2 4

"""
with open('data.txt', 'w') as file:
    for i in range(3):
        file.write(f"{i}\n")

with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

"""
What will be the output in the file?

1. ['Line 0\n', 'Line 1\n', 'Line 2\n']
2. ['Line 0\nLine 1\nLine 2\n']
3. ['Line 1\n', 'Line 2\n', 'Line 3\n']
4. ['Line 1\nLine 2\nLine 3\n']

"""

with open('output.txt', 'w') as f:
    for i in range(3):
        f.write(f"Line {i}\n")

with open('output.txt', 'r') as f:
    content = f.readlines()
print(content)

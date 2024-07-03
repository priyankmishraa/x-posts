"""
What will be the output?

1. 0 red 1 blue 2 green
2. 1 blue 2 green
3. 0 red 2 green
4. red green

"""

data = ['red', 'blue', 'green']
for i, color in enumerate(data):
    if i == 1:
        continue
    print(i, color)

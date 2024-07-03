"""
What will be the output?

1. 0 red 1 green 2 blue
2. 0 red 1 green
3. red green blue
4. green blue

"""
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    if index == 2:
        continue
    print(index, color)

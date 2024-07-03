"""
What will be the output?

1. a 1 b 2
2. a 1 b 2 3
3. b 2
4. a 2 b 3

"""

list1 = ['a', 'b']
list2 = [1, 2, 3]
for char, num in zip(list1, list2):
    if num > 1:
        print(char, num)

"""
What will be the output?

1. 1 a, 2 b, 3
2. 1 a, 2 b
3. a 1, b 2
4. 1 a, 2 b, 3 c

"""

list1 = [1, 2, 3]
list2 = ['a', 'b']
for num, char in zip(list1, list2):
    print(num, char)

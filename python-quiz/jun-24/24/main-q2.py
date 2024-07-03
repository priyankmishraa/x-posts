"""
What will be the output?

1. a 1 b 2 c
2. a 1 b 2
3. a 1 b 2 c 3
4. 1 2 a b

"""
list1 = ['a', 'b', 'c']
list2 = [1, 2]
for char, num in zip(list1, list2):
    print(char, num)

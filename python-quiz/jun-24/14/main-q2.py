"""
What will be the output?

1. Anna 90 Bob 80
2. Anna 90 Bob 80 70
3. Anna 90 Bob 80 None 70
4. Anna 90 Bob 80 70

"""

names = ['Anna', 'Bob']
scores = [90, 80, 70]
for name, score in zip(names, scores):
    print(name, score)

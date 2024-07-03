"""
What will be the output?

1. John 25, Alice 30, Bob 22
2. John 30, Alice 25, Bob 22
3. John 22, Alice 30, Bob 25
4. 25 John, 30 Alice, 22 Bob

"""

names = ['John', 'Alice', 'Bob']
ages = [25, 30, 22]
for name, age in zip(names, ages):
    print(name, age)

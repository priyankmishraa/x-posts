"""
What will be the output?

1. Tom 5 Jerry 7
2. Jerry 7
3. Jerry 10
4. Tom 5 Jerry 7 10

"""
names = ['Tom', 'Jerry']
ages = [5, 7, 10]
for name, age in zip(names, ages):
    if age > 6:
        print(name, age)

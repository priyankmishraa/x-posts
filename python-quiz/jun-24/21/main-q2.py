"""
What will be the output?

1. 0 1 2 3 While loop completed
2. 0 1 2 3
3. 0 1 2 While loop completed
4. 0 1 2

"""
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("While loop completed")

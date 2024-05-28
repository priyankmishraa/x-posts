"""
What will be the output?
a) 10
b) Error
c) None
d) data.pkl
"""

import pickle

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
with open('data.pkl', 'wb') as f:
    pickle.dump(obj, f)

with open('data.pkl', 'rb') as f:
    loaded_obj = pickle.load(f)

print(loaded_obj.value)

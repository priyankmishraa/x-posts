"""
What will be the output?
a) Bird is flying
Sparrow is flying
Airplane is flying
b) Bird is flying
Bird is flying
Airplane is flying
c) Bird is flying
Sparrow is flying
Error
d) Error
"""
class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def let_it_fly(entity):
    entity.fly()

let_it_fly(Bird())
let_it_fly(Sparrow())
let_it_fly(Airplane())

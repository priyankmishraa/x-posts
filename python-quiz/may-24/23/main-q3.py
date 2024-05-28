"""
What will be the output?
a) 5250
b) 5000
c) Error
d) None
"""

class Employee:
    raise_amount = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_amount)

emp1 = Employee("John", 5000)
emp1.apply_raise()
print(emp1.salary)

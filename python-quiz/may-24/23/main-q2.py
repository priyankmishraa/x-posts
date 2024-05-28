"""
What will be the output?
a) John
6000
b) John
5000
c) John
Error
d) Error
"""

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

emp = Employee("John", 5000)
print(emp.get_name())
emp.set_salary(6000)
print(emp.__salary)

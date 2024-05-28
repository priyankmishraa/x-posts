"""
What will be the output?
a) 2024 5 19
b) Error
c) None
d) 2024 05 19
"""

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

date = Date.from_string("2024-05-19")
print(date.year, date.month, date.day)
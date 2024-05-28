"""
What will be the output?
a) An error occurred
b) Error
c) None
d) CustomError
"""

class CustomError(Exception):
    pass

try:
    raise CustomError("An error occurred")
except CustomError as e:
    print(e)

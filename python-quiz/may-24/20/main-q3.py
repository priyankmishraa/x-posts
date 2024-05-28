"""
What will happen when the last line is executed?
a) Temperature below -273.15 is not possible
b) -300
c) None
d) Error

"""

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

temp = Celsius()
temp.temperature = -300


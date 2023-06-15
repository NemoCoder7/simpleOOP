import math


class Mathematics:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_all(self):
        return f" a+b= {self.a + self.b} \n a-b= {self.a - self.b} \n a*b= {self.a * self.b} \n a/b= {self.a / self.b} \n lg(a)= {math.log10(self.a)} \n a^b= {math.pow(self.a, self.b)}"


calculator = Mathematics(13, 7)
print(calculator.calculate_all())

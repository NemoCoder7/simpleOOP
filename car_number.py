class CarNumber:
    def __init__(self, number):
        self.number = number

    def is_number(self):
        if len(self.number) == 6 and self.number[0].isalpha() and self.number[1:4].isdigit() and self.number[4:].isalpha():
            return f'{self.number.upper()} is correct (normal)'
        elif len(self.number) == 6 and self.number[:3].isdigit() and self.number[3:].isalpha():
            return f'{self.number.upper()} is correct (advanced)'
        else:
            return f'{self.number.upper()} is incorrect'

number_plate = input("Enter the car number plate: ")
car = CarNumber(number_plate)
result = car.is_number()
print(result)

class CalcCredit:

    def __init__(self, deposit, years, percentage=4):
        self.deposit = deposit
        self.years = years
        self.percentage = percentage

    def calcdeposite(self):
        while self.years:
            self.deposit += self.deposit * self.percentage / 100
            self.years -= 1
        return self.deposit


credit = CalcCredit(1000, 3)
print(credit.calcdeposite())

class CashCalculator:

    def __init__(self, cash: int):
        self.cash = cash

    def calculator_cash(self):
        x = self.cash // 100
        if x > 0:
            y = (self.cash % 100) // 50
            if y > 0:
                z = (self.cash % 50) // 25
                if z > 0:
                    a = (self.cash % 25) // 10
                    if a > 0:
                        b = (self.cash % 10) // 5
                        if b > 0:
                            c = (self.cash % 5) // 1
        return f"{x} dolLars, {y} 50 cents, {z} 25 cents, {a} 10 cents, {b} 5 cents, {c} 1 cents"


t = CashCalculator(498)
print(t.calculator_cash())

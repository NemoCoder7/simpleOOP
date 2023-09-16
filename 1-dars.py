class Point:
    """Nuqtani ifodalovchi klass"""
    a = "secret"

    def set_coords(self, x, y):
        self.x = x
        self.y = y


point1 = Point()
point1.set_coords(10, 20)
# print(getattr(point1, "a")) // obj-ga qiymatni oladi
# print(setattr(point1, "a", "a secret")) // obj-ga qiymatni qo'shadi
# print(hasattr(point1, "a")) // obj-dan qiymatni bor yoy'qligini tekshiradi
# print(point1.__dict__)
# print(delattr(point1, "a")) // obj-dan qiymatni o'chiradi
# print(point1.__dict__)
# print(hasattr(point1, "a"))
# print(Point.__doc__)
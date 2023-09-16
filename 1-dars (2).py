# class Point:
#     """Nuqtani ifodalovchi klass"""
#     a = "secret"

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y


# point1 = Point()
# point1.set_coords(10, 20)
# print(getattr(point1, "a")) // obj-ga qiymatni oladi
# print(setattr(point1, "a", "a secret")) // obj-ga qiymatni qo'shadi
# print(hasattr(point1, "a")) // obj-dan qiymatni bor yoy'qligini tekshiradi
# print(point1.__dict__)
# print(delattr(point1, "a")) // obj-dan qiymatni o'chiradi
# print(point1.__dict__)
# print(hasattr(point1, "a"))
# print(Point.__doc__)

# initializer , finalizer 

# __sadasd__ -> metodlar, magic metodlar deb ataladi

# __init__(self) -> initializer classdan yaratilgan obyektimizning
# __del__(self) -> finalizator classning

# class Point:
#     """Nuqtani ifodalovchi klass"""
#     a = "secret"

#     def __init__(self, x=0, y=0):
#         """ object yaralgangan keyin srazu ishlaydi"""
#         print("Init metodi ishladi")
#         self.x = x
#         self.y = y

#     def __del__(self):
#         """ objectdan ssilka yuqolsa ya'ni object boshqa ishlatilmasa bu metod ishlaydi va xotiradan obj uchadi"""
#         print("Biz yaratgan obj xotiradan  o'chirildi")

#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y

#     def get_coords(self):
#         return self.x, self.y


# pt1 = Point(3, 4)
# print(pt1.__dict__)

class Point:
    def __new__(cls, *args, **kwargs):
        print("__new metodi ishladi")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("__init__ metodi ishladi")
        self.x = x
        self.y = y

    
pt = Point(3, 4)
print(pt)

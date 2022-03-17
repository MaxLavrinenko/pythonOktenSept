# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон
#
# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return f'сума площадей : {(self.x * self.y) + (other.x * other.y)}'
#
#     def __sub__(self, other):
#         return f'разница площадей : {(self.x * self.y) - (other.x * other.y)}'
#
#     def __eq__(self, other):
#         return f'или площади равны: {(self.x * self.y) == (other.x * other.y)}'
#
#     def __ne__(self, other):
#         return f'не равны: {(self.x * self.y) != (other.x * other.y)}'
#
#     def __gt__(self, other):
#         return f' > : {(self.x * self.y) > (other.x * other.y)}'
#
#     def __lt__(self, other):
#         return f' < : {(self.x * self.y) < (other.x * other.y)}'
#
#     def __len__(self):
#         return (self.x + self.y) * 2
#
#
# rectangle1 = Rectangle(3, 6)
# rectangle2 = Rectangle(4, 6)
#
# print((rectangle1 + rectangle2))
# print((rectangle1 - rectangle2))
# print((rectangle1 == rectangle2))
# print((rectangle1 != rectangle2))
# print((rectangle1 > rectangle2))
# print((rectangle1 < rectangle2))
# print(len(rectangle1))


#   ###############################################################################
#
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderela(Human):
    count = 0

    def __init__(self, name, age, shoe):
        super().__init__(name, age)
        self.shoe = shoe
        Cinderela.count += 1

    @classmethod
    def getCount(cls):
        return print('count of Cinderelas : ', cls.count)

    def print(self):
        return print(f'your Cinderelas is {self.name} shes age {self.age}')


class Prince(Human):
    def __init__(self, name, age, findShoe):
        super().__init__(name, age)
        self.findShoe = findShoe

    def find(self, list: list[Cinderela]):
        for i in list:
            if i.shoe == self.findShoe:
                i.print()


girls = [
    Cinderela('Karina', 25, 38),
    Cinderela('Katya', 30, 41),
    Cinderela('Arina', 35, 45)
]
prince = Prince('Vasya', 30, 41)
prince.find(girls)

Cinderela.getCount()

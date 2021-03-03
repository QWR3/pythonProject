# 1)
# создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька
# class Human:
#     def __init__(self, age, name, size):
#         self.age = age
#         self.name = name
#         self.size = size
#
#
# class Prince(Human):
#     def __init__(self, age, name, size, list):
#         super().__init__(age, name, size)
#         self.list = list
#         for i in self.list:
#             if i['size'] == size:
#                 print(i['name'])
#
#
# class Cinderella(Human):
#     def __init__(self, age, name, size):
#         super().__init__(age, name, size)
#
#
# cinderella = Cinderella(14, 'cinderella', 38)
# fake_cinderella = Cinderella(34, 'fake', 43)
# fake_cinderella2 = Cinderella(32, 'fake', 42)
# prince = Prince(15, 'prince', 38, [cinderella.__dict__, fake_cinderella.__dict__, fake_cinderella2.__dict__])
#
#
# 2)
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.xy = self.x * self.y
#
#     def __add__(self, other, ):
#         return self.xy + (other.x * other.y)
#
#     def __sub__(self, other):
#         return self.xy - (other.x * other.y)
#
#     def __eq__(self, other):
#         return self.xy == (other.x * other.y)
#
#     def __ne__(self, other):
#         return self.xy != (other.x * other.y)
#
#     def __lt__(self, other):
#         return self.xy < (other.x * other.y)
#
#     def __gt__(self, other):
#         return self.xy > (other.x * other.y)
#
#     def __len__(self):
#         return self.x + self.y
#
#
# one = Rectangle(6, 7)
# two = Rectangle(4, 5)
# print(one!=two)
# print(len(one))


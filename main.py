#   - найти min число в листе
# l = [22, 3,5,2,8,2,-23, 8,23,5]
# min = min(l)
# print(min)
#
#   - удалить все одинаковые значения
# l = [22, 3, 5, 2, 8, 2,-23, 8, 23, 5]
# i = 0
# for i in l:
#     if l.count(i) > 1:
#         del(l[i])
#     print(i)
#
#   - заменить каждое четвертое значение на "Х"
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# i = 0
# while i < len(l):
#     i = i + 4
#     if i < len(l):
#         del l[i]
#         l.insert(i, 'X')
# print(l)

# - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа пример:
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# serAr = round(sum(l) / len(l))
# minus =[]
# i = 0
# while i < len(l):
#     minus.append(serAr - l[i])
#     if minus[i] < 0:
#         minOnMinOne = minus[i] * (-1)
#         minus.pop(i)
#         minus.insert(i, minOnMinOne)
#     i = i + 1
# m = min(minus)
# index=minus.index(m)
# result =l[index]
# print(result)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# h = int(input('height'))
# w = int(input('weight'))
# a= 0
#
# while a < h:
#     b = 0
#     if a !=0 and a !=h-1:
#         print('*', end='')
#         while b < w - 2:
#             print(' ', end='')
#             b = b + 1
#         print('*', end='')
#     else:
#         while b < w:
#             print('*' , end='')
#             b = b + 1
#
#     print(" ")
#     a = a + 1


# 3) переделать первое задание под меню с помощью цикла
print('1 - найти min число в листе')
print('2 - удалить все одинаковые значения')
print('3 - заменить каждое четвертое значение на "Х"')
print('4 - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа')
inp = int(input('сделайте ваш выбор:'))
#   - найти min число в листе
if inp == 1:
    l = [22, 3,5,2,8,2,-23, 8,23,5]
    min = min(l)
    print(min)

  # - удалить все одинаковые значения
if inp == 2:
    l = [22, 3, 5, 2, 8, 2,-23, 8, 23, 5]
    i = 0
    for i in l:
        if l.count(i) > 1:
            del(l[i])
        print(i)

      # - заменить каждое четвертое значение на "Х"
    l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    i = 0
    while i < len(l):
        i = i + 4
        if i < len(l):
            del l[i]
            l.insert(i, 'X')
    print(l)

# - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа пример:
if inp == 3:
    l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    serAr = round(sum(l) / len(l))
    minus =[]
    i = 0
    while i < len(l):
        minus.append(serAr - l[i])
        if minus[i] < 0:
            minOnMinOne = minus[i] * (-1)
            minus.pop(i)
            minus.insert(i, minOnMinOne)
        i = i + 1
    m = min(minus)
    index=minus.index(m)
    result =l[index]
    print(result)


# 4) вывести табличку умножения с помощью цикла while
# a=1
# while a<=10:
#     b=1
#     while b<=10:
#         c=a*b
#         print(c, end=" ")
#         b+=1
#     print("")
#     a+=1

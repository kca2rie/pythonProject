# Задача 1 Программа, проверяющая введенное целое число на четность

# num = int(input())
# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# Задача 2 Написать слово "КОПЕЕК" в правильном формате (диапазон от 1 до 99)

# # Задача 3 Написать программу "калькулятор"

# a, b = int(input()), int(input())
# c = input()
# if c == '+':
#     print(a+b)
# elif c == '-':
#     print(a-b)
# elif c == '*':
#     print(a*b)
# elif c == '/' and b != 0:
#     print(a/b)
# elif c == '/' and b == 0:
#     print('На ноль делить нельзя!')
# else:
#     print('Неверная операция')

# # Задача 4 Программа нахождения максимального значения из трех чисел (тернарное выражение)

# a, b, c = int(input()), int(input()), int(input())

# if a>b and a>c:
#     print("Максимальное значение:",a)
# elif b>a and b>c:
#     print("Максимальное значение:",b)
# else:
#     print("Максимальное значение:",c)

# 2.10.2021
# задача1 программу, которая выводит на экран линию из символов.Пользователь указывает: число символов, тип символа и ориентацию линии - вертикальную или горизонтальную.

# a = int(input("Количество символов: "))
# b = input("Тип символов: ")
# c = int(input("Ориентация линии: "))
# if c == 1:
#     for i in range(a):
#         print(b)
# else:
#     print(a * b)


# задача2 программу,которая вычисляет среднее арифметическое последовательности дробных чисел. Программа должна вывести мин и макс число последовательности.

# n = int(input("Введите количество чисел последовательности: "))

# a = float(input("Введите число: "))
# b = float(input("Введите число: "))
# c = float(input("Введите число: "))
# d = float(input("Введите число: "))
# f = float(input("Введите число: "))

# print("Количество чисел:", n)

# average = (a+b+c+d+f)/5
# print("Среднее арифметическое:", average)

# minimum = min(a,b,c,d,f)
# maximum = max(a, b, c, d, f)
# print("Минимальное число:", min(a,b,c,d,f))
# print("Максимальное число:", max(a,b,c,d,f))


# задача 3 программу, которая определяет являются ли они палиндромами и выводит их на экран.
# n = int(input("Введите число "))


# 3.10.2021
# # задача 1 Выведите все элементы списка с четными индексами.

# n = [5, 1, 9, 7, 6, 3]
# print(n[0], n[2], n[4])


# задача 2 Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# n = [2, 9, 4, 6, 3, 5]
# x = 1
# while x != len(n):
#     if n[x] > n[x-1]:
#         print(n[x], end=" ")
# b += 1

# # задача 3 Дан список. Выведите те его элементы, которые встречаются в списке только один раз.

# a = [int(s) for s in input().split()]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')

# 16.10.2021
# Задача 1 программу заполнения списка пол.и отр. элем. Из него треб.сформ.новый массив только из полож.элем. Найти наибольш.эдлем. Распечатать новый массив и наибольш.элемент.

# s1 = []
# n = int(input("Введите длину списка: "))
# for num in range(n):
#     x = int(input("Введите элемент списка: "))
#     s1.append(x)
# print("Список: ", s1)
# s2 = []
# for x in s1:
#     if (x >= 0):
#         s2.append(x)
# print("Новый список, состоящий из положительных элементов:", s2)
# maxim = max(s2)
# print("Наибольший элемент списка:", maxim)
#
# # Задача 2 Вставить в список на позицию c индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
#
# s1 = []
# n = int(input("Введите элементы списка: "))
# for num in range(n):
#     x = int(input("-> "))
#     s1.append(x)
# k = int(input("Введите индекс: "))
# c = int(input("Введите значение: "))
# s1.insert(k,c)
# print(s1)
#
# # Задача 3 Сформировать список квадратов чисел от 1 до 10 (с помощью метода append())
#
# b = []
# i = 1;
# while i <= 10:
#     b.append(i*i)
#     i = i + 1
#
# print("b = ", b)

# 17.10.2021
# Задача 1 программу, вычисляющую расстояние между двумя точками плоскости (x1,y1) и (x2,y2) на основании их координат.

# x1 = int(input("Введите x1: "))
# x2 = int(input("Введите x2: "))
# y1 = int(input("Введите y1: "))
# y2 = int(input("Введите y2: "))
#
# from math import sqrt
#
# distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
#
#
# print("Расстояние между точками:", distance)
#
# # Задача 2 Вычислите площадь треугольника по сторонам и углу между ними
#
# a = int(input("Сторона 1: "))
# b = int(input("Сторона 2: "))
# c = int(input("Угол: "))
# from math import sin
# s = 0.5 * (a * b) * sin(c)
# print("Площадь треугольника:", s)

# 23.10
# Задача 1 Функции нахождения площади фигур: прямоугольник, треугольник, круг

# import math
#
# def rectangle(a, b):
#     return a * b
#
# def triangle(a, b, c):
#     p = (a+b+c) / 2
#     return math.sqrt(p * (p-a) * (p-b) * (p-c))
#
# def circle(r):
#     return math.pi * r**2
#
# choice = input("Прямоугольник (1), треугольник (2), круг (3): ")
# if choice == "1":
#     l = float(input("Длина: "))
#     w = float(input("Ширина: "))
#     print("Площадь прямоугольника: ", rectangle(l,w))
#
# elif choice == "2":
#     a = float(input("Первая сторона: "))
#     b = float(input("Вторая сторона: "))
#     c = float(input("Третья сторона: "))
#     print("Площадь треугольника: ", triangle(a, b, c))
#
# elif choice == "3":
#     r = float(input("Радиус: "))
#     print("Площадь круга: ", circle(r))

# Задача 2 Дан список целых чисел. Найти минимальное среди простых чисел и максимальное среди чисел, не являющихся простыми

# num = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# min(num)
# max(num)
# primes = [num for num in range(min, max) if 0 not in [num % i for i in range(2, int(num/2)+1)]]
#
# print(primes)

# Задача 3
# def get_sum(n):
#     summa = 0
#     if n > 0:
#         for i in str(n):
#             if int(i) % 2 == 0:
#                 summa += int(i)
#     print("Сумма четных чисел:", summa)

# 24.10
#  Задача 1

# def get_num(*nums):
#     max1 = 0
#     for i in nums:
#         if i > max1 and i % 13 == 0:
#             max1 = i
#     print(max1)
#
#     return max1


# get_num(99, 39, 100, 34)

# Задача 2 поиск заданного элемента в кортеже

# tupleObj = ('ab', 'abcd', 'cde', 'abc', 'def')
# if 'ab' in tupleObj:
#     print('YES')

# Задача 3 Введите статистику частотности символов в кортеже

# s = tuple('253523651')
# print(s)
# print(s.count('2'))
# print(s.count('5'))
# print(s.count('3'))
# print(s.count('6'))
# print(s.count('1'))


# 30.10
# Задача 1 Найти все буквы в первой строке, которые отсутствуют во второй

# a = 'Python'
# b = 'Programming language'
#
# aset = set(a)
# bset = set(b)
# c = aset.difference(bset)
# print("Искомыми буквами явл:", c)

# Задача 2 Посчитать гласные буквы в строке

# a = 'Привет, мир!'
# aset = set(a)

# Задача 3 Найти все буквы, присутстсвующие хотя бы в одной строке

# a = 'test'
# b = 'string'
# aset = set(a)
# bset = set(b)
# c = aset.union(bset)
# print(c)

# Задача 4 Вывод уникальных букв из 2х строк

# a = 'hello'
# b = 'world'
# aset = set(a)
# bset = set(b)
#
# res = aset.symmetric_difference(bset)
# print(res)

# 21/11
# Задача 1 Удаление буквы из слова, заданй номером позиции

# def DelCharAtPos(s, pos):
#     if (pos < 0) or (pos >= len(s)):
#         return s
#
#     return s[:pos] + s[pos + 1:]
#
#
# s = "0123456789"
# s2 = DelCharAtPos(s, 4)
# print("s = ", s)
# print("s2 = ", s2)

# Задача 2 Удаление всез вхождений заданного символа из строки

# def DelChar(s, c):
#     s2 = ""
#
#     for sym in s:
#         if sym != c:
#             s2 += sym
#     return s2


# s = "012345363738494"
# s2 = DelChar(s, '3')
# print("s = ", s)
# print("s2 = ", s2)

# Задача 3 функция перевода десятичного числа в двоичное

# def binary(n):
#     s = ''
#     while n > 0:
#         s = str(n % 2) + s
#         n //= 2
#     return s
#
#
# while 1:
#     n = int(input())
#     if n != 0:
#         print(binary(n))
#     else:
#         break

# 27/11
# Задача 1 Найти номер телефона в формате +7хххххххххх или 7хххххххххх
# import re
#
# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# print(re.findall(r'[+]\d+', d))

# Задача 2 ПРоверка соответствия пароля.

# Задача 3 Найти дату в формате dd/mm/YYYY

# str = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, быди зафиксированы максимумы ежемесячных осадков."
# reg = r'\d{2/2/4}'
# print(re.findall(reg, str))

# 4/12
# Задача 1 Вычисоить кол-во отрицательных чисел в списке [-2, 3, 8, -11, -4, 6], n = 3

# def CalcSumNegativeNumbers(A):
#     if not A:
#         return 0
#     else:
#         count = CalcSumNegativeNumbers(A[1:])
#
#         if A[0] < 0:
#             count = count + 1
#
#         return count
#
#
# L = [-2, 3, 8, -11, -4, 6]
#
# n = CalcSumNegativeNumbers(L)
#
# print("n =", n)


# Задача 2 Программа принимает на вход список, состоящий из других списков, и возвращает обычный список, в котором присутсвуют все элементы из вложенных списков


# def flatten(names):
#     if not names:
#         return names
#     if isinstance(names[0], list):
#         return flatten(names[0]) + flatten(names[1:])
#     return names[:1] + flatten(names[1:])
#
#
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print("Выпрямленный список: ", flatten(names))


# 11/12
# Задача 1 есть список из 10 элементов, заполненный случайными числами. Необходимо найти число введенное пользователем

# from random import randint
#
#
# def seq_search(s, item):
#     s.sort()
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [52, 99, 6, 58, 78, 31, 94, 36, 23, 86]
# print(lst)
# num = int(input("Введите число: "))
# print(seq_search(lst, num))
# if seq_search(lst, num):
#     print(f"Число {num} в списке присутствует")
# else:
#     print(f"Число {num} в списке отсутствует")

# 12/12
# Задача 1 Обмен местами двух строк в файле

# pos1 = int(input('pos1 = '))
# pos2 = int(input('pos2 = '))
# if pos2 <= pos1:
#     exit()
# f = open('TextFile1.txt', 'r')
# L = f.readlines()
# s = L[len(L)-1]
# length = len(s)
# f_nl = True
# if (length > 0) and ((s[length - 1] != '\n')):
#     L[len(L)-1] += '\n'
#     f_nl = False
# f.close()
# if (pos1<0)or(pos1>=len(L))or(pos2<0)or(pos2>=len(L)):
#     exit()
# s = L[pos1]
# L[pos1] = L[pos2]
# L[pos2] = s
# f = open('TextFile1.txt', 'w')
# if f_nl == False:
#     L[len(L)-1] = L[len(L)-1][:-1]
# for item in L:
#     f.write(item)
# f.close()

# Задача 2 Реверсирование строк файла (перестановка строк файла в обратном порядке)

# f = open('TextFile1.txt', 'r')
# L = f.readlines()
# s = L[len(L)-1]
# length = len(s)
# f_nl = True
# if (length>0)and((s[length-1] != '\n')):
#     L[len(L)-1] += '\n'
#     f_nl = False
# f.close()
#
# L2 = []
# i = 0
# while i < len(L):
#     s = L[len(L) - i - 1]
#     L2 = L2 + [s]
#     i += 1
#
# if f_nl == False:
#     L2[len(L)-1] = L2[len(L)-1][:-1]
#
# f = open('TextFile1.txt', 'w')
# for item in L2:
#     f.write(item)
#
# f.close()
#
# # Задача 3 Объединение двух файлов
# f1 = open('myfile1.bin', 'rb')
# f2 = open('myfile2.bin', 'rb')
# L1 = f1.readlines()
# L2 = f2.readlines()
# L3 = L1 + L2
# f1.close()
# f2.close()
# f3 = open('myfile3.bin', 'wb')
# f3.writelines(L3)
# f3.close()

# 18.12.2021
# Задача. Вывести на экран сначала все файлы а затем все директории расположенные в корневой директории дерева python

import os
print(os.listdir())
for dirs in os.walk("test", topdown=True):
    print("Subdirs:", dirs)

# 25.12.21
# Задача 1 Реализуйте класс "Книга". Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр,
# автора, цену. Реализуйте методы класса для ввода данных, вывода данных,реализуйте доступ к отдельным полям через методы класса.

class Book:
    name = "name"
    year = "0000"
    publisher = "publisher"
    genre = "genre"
    author = "author"
    price = "price"

    def print_info(self):
        print(f"Название: {self.name}\nГод выпуска: {self.year}\n"
              f"Издатель: {self.publisher}\nЖанр: {self.genre}\n"
              f"Автор: {self.author}\nЦена: {self.price}")

    def input_info(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

h1 = Book()
h1.input_info("Мёртвые души", "1835", "Азбука", "Поэма", "Гоголь Н.В", "252")
h1.print_info()
h1.set_name("")
print(f"Имя: {h1.get_name()}")
h1.set_year("")
print(h1.get_year())
h1.set_publisher("")
print(h1.get_publisher())
h1.set_genre("")
print(h1.get_genre())
h1.set_author("")
print(h1.get_author())
h1.set_price("")
print(h1.get_price())


# 26/12/21
# Задача. Разработать класс Sphere для представления сферы в трехмерном пространстве. Создать в классе набор методов.

from math import pi


class Sphere:
    def __init__(self, *arg):
        if len(arg) == 0:
            arg = (1, 0, 0, 0)
        elif len(arg) == 1:
            arg = (arg[0], 0, 0, 0)
        else:
            raise TypeError
        self.r, self.x, self.y, self.z = arg

    def get_volume(self):
        return (self.r ** 3) * pi * 4 / 3

    def get_square(self):
        return (self.r ** 2) * pi * 4

    def get_radius(self):
        return self.r

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.r = r

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.r ** 2

    
    
    
    # Долги
# 31/10
# Задача 1. дано три словаря. объединить данные словари в один

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}
d4 = d1 | d2 | d3
print(d4)

# Задача 2 Дан словарь. Измените значение зарплаты Бреда с 6500 на 8500.

dict1 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
lst = input("lst ")
salary = input("salary ")
print(dict1[lst][salary])
num = input("numbers ")

dict1[lst][salary] = num
print(dict1[lst])

# Задача 3 Пользователь вводит данные о кол-ве студентов: их фимилии, имена и балл. Программа должна определить средний балл и вывести фамилии и имена студентов, чей балл выше среднего.

studs = {}
n = int(input("Количество студентов: "))
s = 0
for i in range(n):
    sname = input(str(i+1) + "-й студент: ")
    point = int(input("Балл: "))
    studs[sname] = point
    s += point

avrg = s / n
print("\nСредний балл: %.0f. Студенты с баллом выше среднего:" % avrg)
for i in studs:
    if studs[i] > avrg:
        print(i)
# 13.11.21
        
# 14.11.21
# Задача 1 Создать функцию, которая будет находить сумму любого кол-ва чисел и декоратор, который будет находить среднее арифметическое этих чисел.

def my_decorator(func):
    def wrap(*args):
        res = func(*args)
        return res

    return wrap

@my_decorator
def func_test(a, b, c, d):
    return a + b + c + d


print("Сумма чисел 2, 3, 3, 4 =", func_test(2, 3, 3, 4))


# Задача 3 Дан список чисел. С помощью lambda-выражения возведите в квадрат и в куб все илементы данного списка.

nums = [3, 5, 7, 3, 9, 5, 7, 2]

square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)

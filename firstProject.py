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
# Задача 2 Создать ламбда-выражение для вычисления суммы трех чисел, с использованием вложенных ламбда-выражений

print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))

# Зачача 3 Отсортировать список объектов по имени студентов и итоговым оценкам в порядке убывания

students = [{'name': 'Jennifer', 'final': 95},
         {'name': 'David', 'final': 92},
         {'name': 'Nicolas', 'final': 98}]

print(sorted(students, key=lambda item: item['name']))
print(sorted(students, key=lambda item: item['final'], reverse=True))        
    
    
    
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


# 9/01/2022
# создайте класс для конвертирования температуры из цельсия в фаренгейт и наоборот.
# У класса должно быть два статистических метода. Также класс должен считать количествоподсчетов температуры и возвращать это значение с помощью статистического метода.


class Convert:
    @staticmethod
    def tf(x):
        tf = (9 / 5) * x + 32
        return tf

    @staticmethod
    def tc(y):
        tc = (9 / 5) * y - 32
        return  tc
    print('t в цельсиях', tc, 'т в фаренгейтах', tf)
    
    
# 15.01.2022
# Создать класс Liquid со свойствами: название и плотность жидкости, - и методами: изменение плотности, вычисление объема жидкости, соответствующего заданной массе, вычисление массы жидкости, соответствующий заданному объему, вывод информации о жидкости.
# Создать производный класс Alcohol с собственным свойством - крепость, - и методом: изменение крепости.

class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def edit_density(self, val):
        self.density = val

    def calc_v(self, m):
        v = round(m / self.density, 2)
        print(f'Объём {m} кг {self.name} равен {v} m^3.')
        return v

    def calc_m(self, v):
        m = v * self.density
        print(f'Вес {v} m^3 {self.name} составляет {m} кг.')
        return m

    def print_info(self):
        print(f'Жидкость {self.name!r} (плотность = {self.density} kg/m^3).')

class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def edit_strength(self, val):
            self.strength = val


a = Alcohol('Wine', 1064.2, 14)
a.print_info()
a.edit_density(1000)
a.print_info()
print()
a.calc_m(0.5)
a.calc_v(300)
print()
print(a.strength)
a.edit_strength(20)
print(a.strength)

# 16.01
# Задача создайте базовый абстрактный класс Корень с методами вычисления корней уравнения и вывода результата на экран.
# Реализуйте производные классы Линейное уравнение и Квадратное уравнение с собственными методами вычисления корней и вывода на экран.

 from abc import ABC, abstractmethod
    
    
class Root(ABC):
    def __init__(self, val_1, val_2):
        self.val_1 = val_1
        self.val_2 = val_2

    def calculate_linear_equation(self):
        root = -self.val_2 / self.val_1
        return root

    def quad_equation(self):
        disc = self.val_2 * 2 + 4 * self.val_1 * 3
        root_1 = (self.val_2 + math.sqrt(disc)) / (2 * self.val_1)
        root_2 = (self.val_2 - math.sqrt(disc)) / (2 * self.val_1)
        return root_1, root_2

    @abstractmethod
    def print_info(self):
        raise NotImplementedError


class Linear(Root):
    def __init__(self, val_1, val_2):
        super().__init__(val_1, val_2)

    def print_info(self):
        print(f"The root of {self.val_1}x+{self.val_2}=0 is: {round(self.calculate_linear_equation(), 2)}")


class Quad(Root):
    def __init__(self, val_1, val_2):
        super().__init__(val_1, val_2)

    def print_info(self):
        print(f"The roots of {self.val_1}x^2-{self.val_2}x-3=0 are: {self.quad_equation()}")


l = Linear(3, 7)
l.print_info()

w = Quad(1, 2)
w.print_info()


# 22.01
#Задача.Создайте класс Student,который будет содержать имя и распечатывать информацию,а также вложенный класс, который будет содержать информацию о ноутбуке с техническими характеристиками: модель, процессор и память

from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, name):
        self.name = name

    class Laptop:
        def __init__(self, model, processor, memory):
            self.model = model
            self.processor = processor
            self.memory = memory


name = Student('Roman')
laptop = name.Laptop('HP', 'i7', '16')
print()


# 23.01
class Clock:
    __DAY = 86400

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целым числом")
        self.secs = secs % self.__DAY

    def get_format_time(self):
        s = self.secs % 60  # секунды
        m = (self.secs // 60) % 60  # минуты
        h = (self.secs // 3600) % 24  # часы
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise AttributeError("Правый операнд должен быть типом данных Clock")
        return Clock(self.secs + other.secs)

    def __eq__(self, other):
        return self.secs == other.secs

    def __ne__(self, other):
        return  not self.__eq__(other)

    def __le__(self,other):
        return self.secs <= other.secs

    def __lt__(self, other):
        return self.secs < other.secs

    def __gt__(self, other):
        return self.secs > other.secs

    def __ge__(self, other):
        return self.secs >= other.secs

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")
        if item == "hour":
            return (self.secs // 3600) % 24
        elif item == "min":
            return (self.secs // 60) % 60
        elif item == "sec":
            return self.secs % 60
        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, value):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")
        s = self.secs % 60
        m = (self.secs // 60) % 60
        h = (self.secs // 3600) % 24
        if key == "hour":
            self.secs = s + 60 *m + value * 3600
        elif key == "min":
            self.secs = s + 60 * value + h * 3600
        elif key == "sec":
            self.secs = value + 60 * m + h * 3600


c1 = Clock(80000)
print(c1.get_format_time())
c1["hour"] = 10
print(c1["hour"], c1["min"], c1["sec"])


# 29/01
# Задача создать класс Shape и три дочерних класса: Square, Rectangle, Triangle. Родительский класс должен иметь абстрактные методы нахождения периметра, площади, рисования фигуры и вывода информации. С помощью полиморфизма реализуйте вывод информации о дочерних фигурах
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return self.color

    def fig_info(self):
        p = self.perimeter()
        s = self.area()

    @abstractmethod
    def print_info(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, s):
        super().__init__("Square")
        self.s = s

    def get_area(self):
        return self.s**2

    def get_perimeter(self):
        perimeter = self.s * 4
        return perimeter

    def get_info(self):
        p = self.get_perimeter()
        s = self.get_area()
        print(f'Периметр: {self.get_perimeter} площадь = {get_space}')


class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__("Rectangle")
        self.w = w
        self.h = h

    def get_perimeter(self):
        perimeter = self.w * 2 + self.h * 2
        return perimeter

    def get_area(self):
        area = self.w * self.h
        return area

    def get_info(self):
        p = self.get_perimeter()
        s = self.get_area()
        print(f'Периметр: {self.get_perimeter} площадь = {get_space}')


class Triangle(Shape):
    def __init__(self, a, b, c,):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

    def get_area(self):
        area = (self.a + self.b + self.c) * 0.5 * ((self.a + self.b + self.c) * 0.5 - self.a) - ((self.a + self.b + self.c) * 0.5 - self.b) - ((self.a + self.b + self.c) * 0.5 - self.c)
        sqrt1 = math.sqrt(area)

        def get_info(self):
            p = self.get_perimeter()
            s = self.get_area()
            print(f'Периметр: {self.get_perimeter} площадь = {get_space}')


if __name__ == '__main__':
    fig1 = Square(3)
    fig2 = Rectangle(3, 7)
    fig3 = Triangle(11, 6, 6)
    array = [fig1, fig2, fig3]
    for f in array:
        f.fig_info()

                   
# 30/01
# Создать класс треугольник, свойства-длин всех сторон.Правильность задания свойств должны проверяться через дескриптон на ввод положительных целых числовых значений.Предусмотреть в классе методы проверки существоввания треугольника.

class Figure:
    @classmethod
    def verify_side(cls, side):
        if not isinstance(side, int) or side < 0:
            raise TypeError(f"Сторона {side} должна быть целым положительным числом")

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name) # instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_side(value)
        setattr(instance, self.name, value)


class Triangle:
    a = Figure()
    b = Figure()
    c = Figure()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


fig1 = Triangle(2, 5, 6)
print(fig1)



# 5.02
# Задача Создать класс Автомобиль со свойствами бренд, модель, год выпуска и пробег. Он будет иметь метод вывода данных на экран.
# От него будет унаследован класс Электро автомобиль с мощностью батареи 100%. Работа с классами должна быть организована через пакет и модули.

import pickle


class Car:
    a_brand = "Tesla"
    a_model = "T"
    a_year = "2018 год"
    a_odometer = "99000 км"

    def __str__(self):
        return f"{Car.a_brand}\n" \
               f"{Car.a_model}\n" \
               f"{Car.a_year}\n" \
               f"{Car.a_odometer}"


obj = Car()

my_obj = pickle.dumps(obj)
print(f"{my_obj}")

l_obj = pickle.loads(my_obj)
print(f"{l_obj}\n")


class Electric(Car):
    a_power = "power"

    def __str__(self):
        print(f"Этот автомобиль имеет мощность 100%")
        
                
# 6.02

import json

dictionary ={
    "1562358897": {
        "name2": "bdbadbg",
        "tel3": "3017067373"
    },
    "1563020871": {
        "name2": "ebdedge",
        "tel8": "8625723308"
    },
    "2869397933": {
        "name1": "dbgeeff",
        "tel9": "3453953075"
    },
    "5349167552": {
        "name8": "bdfaade",
        "tel7": "9694154763"
    },
    "7029491468": {
        "name3": "gegegge",
        "tel4": "3935195344"
    }
}

json_object = json.dumps(dictionary, indent=4)
print(json_object)


# 13/01

import requests
from bs4 import BeautifulSoup

url = "https://www.kinopoisk.ru/lists/top250/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
films = soup.findAll('div', class_='desktop-rating-selection-film-item')

data = []

for film in films:
    link = "https://www.kinopoisk.ru"+film.find('a', classs_='selection-film-item-meta__link').get('href')
    russian_name = film.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__russian-name').text
    original_name = film.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__original-name').text
    country = film.find('a', class_='selection-film-item-meta__link').find('span', class_='selection-film-item-meta__country').text
    film_type = film.find('a', class_='selection-film-item-meta__link').findAll('span', class_='selection-film-item-meta__film-type').text
    rate = film.find('span', class_='rating__value rating__value_positive').text

    data.append([link, russian_name, original_name, country, film_type, rate])

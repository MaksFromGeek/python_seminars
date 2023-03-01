# some_list = [1, 2, 3, 4, 5, 6]
# for ind in range(0, len(some_list)):
# some_list[ind] = str(some_list[ind])
# print(some_list)


# def square(x):
# return x ** 2
#
#
# new_list = list(map(lambda x: x + 1, some_list))
# print(new_list)

# def even(x):
# return type(x) == int

# new_list = list(filter(lambda x: type(x) == int, some_list))
# print(new_list)


# some_list = [10, 20, 30, 40]
# some_dict = {}
# print(list(enumerate(some_list)))
# for ind, value in enumerate(some_list):
# some_dict[ind] = value
#
# print(some_dict)
#
# for ind in range(0, len(some_list)):
# print(ind, some_list[ind])


# first_list = ('apple', 'orange', 'grape', 'лимон')
# second_list = ['яблоко', 'апельсин', 'виноград']
# print(list(zip(first_list, second_list)))
# for eng, ru in zip(first_list, second_list):
# print(eng, ru)


# 47. У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы
# используется множество раз и вы не хотите ничего сломать):

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
# а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# import random
# import time
# import math
# def transformation(x): return x


# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = values
# print(list(map(transformation, transformed_values)))


# 49. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные
# спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий
# длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из
# пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = piab, где a и b -
# длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и
# сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

# import math
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# new = list(filter(lambda x: x[0] != x[1], orbits))
# new2 = max(map(lambda x: x[0]*x[1]* math.pi, new))
# print(new2)
# print(list(filter(lambda x: x[0]*x[1]* math.pi == new2, new)))

# print(max(list(map(lambda x: x[0] * x[1] * math.pi,
#       filter(lambda x: x[0] != x[1], orbits)))))


# Следующая задача. Дан массив с числами, и целевое значение. Нужно проверить найдутся ли в массиве
# два числа, чья сумма равна целевому значению

# import time
# import random

# summa = 102
# some_list = [90, 19, 48, 24, 12]      # [random.randint(1, 100000) for _ in range(10 ** 6)]

# start = time.perf_counter()
# some_set = set(some_list)
# for el in some_set:
#     if summa - el in some_set:
#         print(el, summa - el)
#         break
# else:
#     print('no')
# end = time.perf_counter()
# print(end - start)

# start = time.perf_counter()
# for el in some_list:
#     if summa - el in some_list:
#         print(el, summa - el)
#         break
# else:
#     print('no')
# end = time.perf_counter()
# print(end - start)


# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют 
# одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение 
# характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и 
# вычисляет его характеристику.

# objects = [90, 19, 48, 24, 12]
# def same_by(characteristic, objects):
#     if len(objects) == 0:
#         return True
#     object_set = set(objects)
#     for i in object_set:
#         if characteristic(objects[i]) % 2 == 0:
#             return False
#     return True
# print(same_by)

# if same_by(lambda x: x % 2, objects):
#     print('same')
# else:
#     print('different')

# Правильное решение:

# def same_by(characteristics, objects):
#     if len(objects) == 0:
#         return True
#     for i in range(len(objects)):
#         if characteristics(objects[i]) != characteristics(objects[0]):
#             return False
#     return True

# values = [2, 4, 6, 10]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


# LESSON 8

# with open('les8test.txt', 'r', encoding='utf-8') as file:
# # text = file.read().splitlines()
# # print(text)
#
# while True:
# line = file.readline()
# if not line:
# break
# print(line.strip())

# Запись данных в несуществующий файл:
# with open('filetest.txt', 'a', encoding='utf-8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')


# Создать файл, добавить в него текст и посчитать количество букв в тексте

import time
# with open('test20.txt', 'r', encoding='utf-8') as file:
# find_letter = input('введите искомую букву: ')
# count = 0

# start = time.time()
# for letter in file.read():
# if letter == find_letter:
# count += 1

# end = time.time()
# print(count)
# print(end - start)


# with open('test20.txt', 'r', encoding='utf-8') as file:
#     find_letter = input('введите искомую букву: ')

#     start = time.time()
#     print(file.read().count(find_letter))
    
#     end = time.time()
#     print(end - start)


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение 
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# Для тех кто сделает, следующим заданием будет: сделать рандоммные элементы в стороннем файле. 
# (В отдельном файле указываются позиции элементов в нашем списке, эти элементы и перемножаются 
# между собой)

# from random import randint
# with open('test20.txt', 'w') as file:
#     for _ in range(10):                  # количество повторов цикла
#         file.write(str(randint(0, 9)) + '\n') # число записывать нельзя, поэтому преобразовываем в строчку
#         spis = []                             # чтобы было построчно, добавляем \n
#         for _ in range(10):                   # сгенерировали список
#             spis.append(randint(1, 10))
#             multi = 1
#     print(spis)
# with open('test20.txt', 'r') as file:
#     for el in file.read().split():
#         multi *= spis[int(el)]
#         print(spis[int(el)])
#         print(multi)

# другое решение
from random import randint
n = int(input('Введите кол-во элементов в списке: '))
some_list = [randint(-n, n) for _ in range(n)]   # сгенерировали список
print(some_list)

with open('test20.txt', 'w', encoding='utf-8') as file:
    for _ in range(randint(1, n)):                # количество повторов цикла
        file.write(str(randint(0, n - 1)) + '\n') # число записывать нельзя, поэтому преобразовываем 
                                                  # в строчку, чтобы было построчно, добавляем \n
with open('test20.txt', 'r', encoding='utf-8') as file:
    mult = 1
    for ind in file.read().splitlines():
        mult *= some_list[int(ind)]
print(mult)


# Задача 3 из ДЗ №8. Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. 
# У нас труб будет больше. Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена 
# заполнения всего бассейна только одной данной работающей трубой (в часах). Затем после пустой строки 
# перечислены трубы, которые будут заполнять бассейн. Сколько минут на это потребуется?

# Номер трубы соответствует номеру строки, в которой записана ее производительность.
# Результат запишите в файл time.txt
# Пример
# Ввод
# 1
# 2
# 3
# (пустая строка)
# 1 2 3
# Вывод: 32.72727272727273

f = open('/Users/maksimpolanin/Desktop/dotnet/python_course/python_seminars/DR8/pipes.txt', 'r')
g = open('/Users/maksimpolanin/Desktop/dotnet/python_course/python_seminars/DR8/time.txt', 'w')
a = [int(st.rstrip()) for st in iter(f.readline, '\n')]
print(60 / sum([1 / a[int(x) - 1] for x in f.readline().split()]), file = g)
f,g.close()




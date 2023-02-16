# Задача 1

# string = 'd g h t r g r h t j h b v f d s d f'
# print(string)

# my_list = string.split()
# my_dict = {}
# new_list = []

# for letter in my_list:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
#     if my_dict.get(letter) > 1:
#         new_list.append(letter + '_' + str(my_dict.get(letter)))
#     else:
#         new_list.append(letter)
#     print(my_dict)
# print(' '.join(new_list))


# Задача 2

# text = input('Введите текст: ').split()
# print(text)
# # text = text.split() # измененную переменную нужно к чему то присвоить (к text), сам текст не меняется
# text = set(text) # меняем тип данных со строки на множество
# print(f'Выведем уникальные элементы {text}')
# print(f'В нашем тексте {len(text)} уникальных слова')


# Задача 3. Дана последовательность чисел. Получить список уникальных элементов заданной
# последовательности. Пример [1, 2, 3, 5, 1, 3, 5, 10]

# string = '1, 2, 3, 5, 1, 3, 5, 10'
# print(f'Дана последовательность чисел: {string}')
# my_list = string.split()
# my_dict = {}
# new_list = []
# for digit in my_list:
#     my_dict[digit] = my_dict.get(digit, 0) + 1
#     if my_dict.get(digit) > 1:
#         new_list.remove(digit)
#     else:
#         new_list.append(digit)
# print(f'Уникальные элементы, встречающиеся всего один раз {new_list}')


# # Код для рисования круга
# # Для любителей графики, может кому пригодится
# from turtle import *
# pensize(10)
# while True:
#     forward(10)
#     left(10)
# exitonclick()

# # тг канал препода с 4 семинара по Питону
# cru code crew


# LESSON_5

# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ...,
# an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи

# def fib(n):
#     if n in [1,2]:
#     #     fib = 0
#     # elif n == 1:
#     #     fib = 1
#     # else:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = int(input())
# # for i in range(n):
# print(fib(n)) # для выполнения предыдущ. строки нужно n заменить на i


# 2. Хакер Василий получил доступ к классному журналу и хочет заменить все свои
# минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но
# наоборот: все максимальные – на минимальные. Пользователь вводит оценки вручную.

# # score = input('Введите ч/з пробел оценки ученика: ').split()
# list_1 = []
# min = 5
# max = 0
# list_1 = [int(input('Введите ч/з пробел оценки ученика: '))]
# for i in list_1:
#     if i < min:
#         min = i
#     if i > max:
#         max = i
# print(min, max)
# print(list_1)

n = int(input('введите количество оценок: '))
list_1 = []
min_mark = 5
max_mark = 0
list_1 = [int(input(f'Введите оценку: ')) for i in range(n)]
for i in list_1:
    if i < min_mark:
        min_mark = i
    if i > max_mark:
        max_mark = i
print(min_mark, max_mark)
print(list_1)

for i in range(len(list_1)):
    if list_1[i] == max_mark:
        list_1[i] = min_mark
print(list_1)


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым





# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и 
# количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# a1, d, n = int(input('1 элемент ')), int(input('разность ')), int(input('количество элементов '))
# progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
# print(progressive)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

min, max = int(input('min ')), int(input('max '))
index = [i for i in range(min -1, max)]
print(index)





# Задача 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что
# задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines, file):
#     if lines > 0:
#         with open(file, encoding='utf-8') as text:
#             find = text.readlines()[lines:] # при-lines: отсчет по индексу
#         for line in find:
#             print(line.strip())
#     else:
#         print('Количество строк не целое положительное')

# read_last(5, '/Users/maksimpolanin/Desktop/dotnet/python_course/python_seminars/DR8/article.txt')
# # read_last(-5, '/Users/maksimpolanin/Desktop/dotnet/python_course/python_seminars/DR8/article.txt')


# Задача 2. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).

# def longest_words(file):
#     with open(file, encoding = 'utf-8') as text:
#         words = text.read().split()
#         max_length = len(max(words, key = len))
#         sought_words = [word for word in words if len(word) == max_length]
#         if len(sought_words) == 1:
#             return sought_words[0]
#         return sought_words

# print('Самое длинное слово:', longest_words('/Users/maksimpolanin/Desktop/dotnet/python_course/python_seminars/DR8/article.txt'))


# Задача 3. Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. 
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

with open('/Users/maksimpolanin/Desktop/dotnet/python_course/python_seminars/DR8/pipes.txt', encoding='utf-8') as file:
    time = file.read().split('\n')
while all(time) is False:
    time.remove('')
pipes = list(map(int, time[-1].split()))
time.remove(time[-1])
pipes = list(map(lambda x: x - 1, pipes))
time = [time[pipe] for pipe in pipes]
with open('/Users/maksimpolanin/Desktop/dotnet/python_course/python_seminars/DR8/time.txt', 'w', encoding='utf-8') as answer:
    answer.write(str(60 / sum(map(lambda x: 1 / float(x), time))))







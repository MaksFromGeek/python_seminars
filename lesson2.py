# a = 'hello'
# for i in a:
#     print(i)

# for ind in range(len(a)):
#     print(a[ind])

# for i in range(3):
#     print('HELLO', end = ' ')


# 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1. Решить задачу используя цикл while

# n = int(input())
# factorial = 1
# while n > 0:
#     factorial = factorial * n
#     n = n - 1
# print(factorial)

# n = int(input())
# fact = 1
# i = 2
# while i <= n:
#     fact *= i
#     i += 1
#     print(fact)


# 11. Дано натуральное число А > 1. Отпределите, каким по счету числом Фибоначи оно является, т.е. 
# выведите такое число n, что ф(n) = а

# fib1 = 1
# fib2 = 1
# n = int(input())
# i = 2
# while fib2 <= n:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1
# if fib1 == n:
#     print(i)
# else:
#     print(-1)

# 0 1 1 2 3 5 8 13

# first_el = 0
# second_el = 1
# number = int(input())
# next_el = first_el + second_el
# i = 3
# while next_el < number:
#     first_el = second_el
#     second_el = next_el
#     next_el = first_el + second_el
#     i += 1
# if next_el == number:
#     print(i)
# else:
#     print(-1)


# 13. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная 
# оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, 
# занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная 
# оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих 
# строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# max_count = 0
# count = 0
# n = int(input())
# for _ in range(n):
#     temp = int(input())
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# if max_count == 0 and count != 0:
#     print(count)
# else:
#     print(max_count)

# from random import randint
# n = int(input())
# i = 0
# warm_days = 0
# while i < n:
#     temp = randint(-50, 51)
#     if temp > 0:
#         warm_days += 1
#     i += 1
#     print(warm_days)


# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов 
# слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных 
# на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза. 
# Все числа натуральные и не превышают 30000.

min_weight = 0
max_weight = 0
count = 0
n = int(input('Введите колличество арбузов '))
for _ in range(n):
    weight = int(input(f'Введите вес арбузов всего {n} раз '))
    if weigth > 0:
        count += 1
    elif weight > 30000: 
            weigth = max_weight
    else:
         if weigth < 30000:
              weigth = min_weight
if min_weight > 0 and max_weight > 0:
    print({max_weight}, {min_weight})
else:
    print(count)

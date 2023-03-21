# 1. Количество чисел
# На вход программе подаются два целых числа a и b
# Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно,
# куб которых оканчивается на 4 или 9.
#
# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b+1):
#     if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
#         counter += 1
# print(counter)


# 2. Сумма чисел
# На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# Напишите программу, которая подсчитывает сумму введенных чисел.
#
# n = int(input())
# total = 0
# for i in range(n):
#     num = int(input())
#     total += num
# print(total)


# 3. Асимптотическое приближение
# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
# (1 + 1\2 + 1\3 + ... + 1\n) - \ln(n)
#
# from math import log
# n = int(input())
# total = 0
# for i in range(1, n+1):
#     total += 1/i
# print(total + log(n))


# 4. Факториал
# На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.
#
# n = int(input())
# total = 1
# for i in range(1, n+1):
#     total *= i
# print(total)


# 5. Без нулей
# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
#
# total = 1
# for i in range(10):
#     num = int(input())
#     if num != 0:
#         total *= num
# print(total)


# 6. Последовательность Фибоначчи 🌶️
# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.
# Последовательность Фибоначчи – это последовательность натуральных чисел, где каждое последующее число является суммой двух предыдущих:
# 1, 1, 2, 3, 5, 8, 13,  21, 34, 55...
#
# n = int(input())
# a, b = 1, 1
# for i in range(n):
#     a, b = b, a + b
#     print(a, end=' ')


# text = input()
# total = 0
# while text != 'стоп':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)


# 7. Количество членов
# На вход программе подается последовательность слов, каждое слово на отдельной строке.
# Концом последовательности является одно из трёх слов: «стоп», «хватит», «достаточно».
# Напишите программу, которая выводит общее количество членов данной последовательности.
#
# word = input()
# count = 0
# while word != 'стоп' and word != 'хватит' and word != 'достаточно':
#     count += 1
#     word = input()
# print(count)


# 8. Пока делимся
# На вход программе подается последовательность целых чисел делящихся на 7, каждое число на отдельной строке.
# Концом последовательности является любое число не делящееся на 7.
# Напишите программу, которая выводит члены данной последовательности.
#
# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())


# num = int(input())
# total = 0
# while num >= 0:
#     total += num
#     num = int(input())
# print(total)


# 9. Количество пятерок
# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке.
# Концом последовательности является любое отрицательное число, либо число большее 5.
# Напишите программу, которая выводит количество пятерок.
#
# num = int(input())
# count = 0
# while 0 < num < 6:
#     if num == 5:
#         count += 1
#     num = int(input())
# print(count)


# 10.Обратный порядок 1
# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.
#
# num = int(input())
# while num != 0:
#     last_num = num % 10
#     print(last_num)
#     num = num // 10


# 11. Обратный порядок
# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
# num = int(input())
# while num != 0:
#     last_n = num % 10
#     num = num // 10
#     print(last_n, end='')


# 12. Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
#
# n = int(input())
# total, total_sum = 0, 0
# total_pro = 1
# last = n % 10
# while n != 0:
#     digit = n % 10       # после цикла буде равно первому числу
#     total_sum += digit
#     total += 1
#     total_pro *= digit
#     a = total_sum / total
#     Sum_digit = digit + last
#     n = n // 10
# print(total_sum, total, total_pro, a, digit, Sum_digit, sep='\n')


# 13.Вторая цифра
# Дано натуральное число n,(n > 9).Напишите программу, которая определяет его вторую (с начала) цифру.
#
# n = int(input())
# second = n % 10
# while n > 9:
#     num = n % 10
#     n = n // 10
# second = num
# print(second)






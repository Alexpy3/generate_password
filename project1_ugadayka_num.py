from random import *

def is_valid(num):  # защита от дураков, нужно внести Число в диапазоне от 1 до 100
    return num.isdigit() and 1 <= int(num) <= 100

number = randint(1, 100)

name = input('Привет, как тебя зовут?\n')
print(f"{name}, Добро пожаловать в игру числовая угадайка!")

total = 0
while True:
    n = input('Введите Ваше число от 1 до 100: ')
    total += 1
    if is_valid(n) == False:
        print('А может быть все-таки введете целое число от 1 до 100?')

    n = int(n)

    if n < number:
        print('Ваше число меньше загаданного, попробуйте еще')
    elif n > number:
        print('Ваше число больше загаданного, попробуйте еще')
    else:
        print('Вы угадали, за', total, 'попыток поздравляем!')
        break
print(f'{name}, Спасибо, что играл в числовую угадайку. Еще увидимся...')


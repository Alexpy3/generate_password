import random

def generate_password(length, chars):   # Функция генерации пароля:
    password = ''
    for i in range(length):
        password += random.choice(chars)

    print(password)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

numbers = int(input('Укажите количество паролей для генерации: '))
len = int(input('Укажите длину одного пароля: '))
need_gigits = input('Включать ли цифры 0123456789? (д = да, н = нет): ')
need_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д = да, н = нет): ')
need_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д = да, н = нет): ')
need_punctuation = input('Включать ли символы !#$%&*+-=?@^_? (д = да, н = нет): ')
need_no_simbols = input('Исключать ли неоднозначные символы il1Lo0O ? (д = да, н = нет): ')

if need_gigits == 'д' or need_gigits == 'да':
    chars += digits
if need_lower == 'д' or need_lower == 'да':
    chars += lowercase_letters
if need_upper == 'д' or need_upper == 'да':
    chars += uppercase_letters
if need_punctuation == 'д'or need_punctuation == 'да':
    chars += punctuation
if need_no_simbols == 'д' or need_no_simbols == 'да':
    for i in 'il1Lo0O':
        chars.replace(i, '')

for _ in range(numbers):               # Генерация нужного количества паролей:
    generate_password(len, chars)

# реализовать без функции
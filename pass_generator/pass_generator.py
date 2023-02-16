#  Генерирует безопасные пароли с возможностью указать длину и состав пароля

from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

numbers_of_pass = input('\nСколько паролей Вы хотите сгенерировать?\n')
while numbers_of_pass.isdigit() == False or int(numbers_of_pass) < 1:
        print('Введите цифру больше или равную 1')
        numbers_of_pass = input()
numbers_of_pass = int(numbers_of_pass)

length_of_pass = input('\nВведите длину пароля. Длина >= 4.\n')
while length_of_pass.isdigit() == False or int(length_of_pass) < 4:
        print('Введите цифру больше или равную 4')
        length_of_pass = input()
length_of_pass = int(length_of_pass)

digits_in_pass = input('\nВключать в пароль цифры? (y/n)\n')
while digits_in_pass.lower() not in 'yn':
        print('Введите "y" или "n"')
        digits_in_pass = input()

uppercase = input('\nВключать ли в пароль заглавные буквы? (y/n)\n')
while uppercase.lower() not in 'yn':
        print('Введите "y" или "n"')
        uppercase = input()

lowercase = input('\nВключать ли в пароль строчные буквы? (y/n)\n')
while lowercase.lower() not in 'yn':
        print('Введите "y" или "n"')
        lowercase = input()

symbols = input('\nВключать ли в пароль символы "!#$%&*+-=?@^_"? (y/n)\n')
while symbols.lower() not in 'yn':
        print('Введите "y" или "n"')
        symbols = input()

exceptions = input('\nИсключать ли неоднозначные символы "il1Lo0O"? (y/n)\n')
while exceptions.lower() not in 'yn':
        print('Введите "y" или "n"')
        exceptions = input()

def not_in_exception_char(stroka):
    char = 'i'
    while char in 'il1Lo0O':
        char = choice(stroka)
    return char

def mix_password(password):
    list_pass = list(password)
    shuffle(list_pass)
    mix_pass = ''
    for i in range(len(list_pass)):
        mix_pass += list_pass[i]
    return mix_pass

for i in range(numbers_of_pass):
    chars = ''
    count = 0
    while count <= length_of_pass:
        if digits_in_pass == 'y':
            if exceptions == 'y':
                chars += not_in_exception_char(digits)
                count += 1
            else:
                chars += choice(digits)
                count += 1
        if uppercase == 'y':
            if exceptions == 'y':
                chars += not_in_exception_char(uppercase_letters)
                count += 1
            else:
                chars += choice(digits)
                count += 1
        if lowercase == 'y':
            if exceptions == 'y':
                chars += not_in_exception_char(lowercase_letters)
                count += 1
            else:
                chars += choice(digits)
                count += 1
        if symbols == 'y':
            chars += choice(punctuation)
            count += 1

    print(f'Пароль{i+1}: {mix_password(chars)}')
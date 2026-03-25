from random import sample # импортируем функцию sample() из модуля random

def is_answer(ans): # функция проверки ответа
    if ans.strip().lower() in ['да', 'д', 'yes', 'y']:
        return True
    else:
        return False

def is_digital(number): # функция проверки на ввод числа
    num = number.strip()
    while True:
        if not num.isdigit() or int(num) == 0:
            print('Некорректные данные, введите число!')
            num = input('Введите число: ').strip()
        else:
            return int(num)

def is_safe(password): # проверка безопасности пароля
    cnt_digits, cnt_uppercase_letters, cnt_lowercase_letters, cnt_punctuation = False, False, False, False
    for char in password:
        if char.isupper():
            cnt_uppercase_letters = True
        elif char.islower():
            cnt_lowercase_letters = True
        elif char.isdigit():
            cnt_digits = True
        elif not char.isalnum():
            cnt_punctuation = True

    # Собираем результаты проверки
    results = []
    if len(password) < 10:
        results.append("длина пароля менее 10 символов")
    if not cnt_uppercase_letters:
        results.append("отсутствуют заглавные буквы")
    if not cnt_lowercase_letters:
        results.append("отсутствуют строчные буквы")
    if not cnt_digits:
        results.append("отсутствуют цифры")
    if not cnt_punctuation:
        results.append("отсутствуют специальные символы")

    if results:
        return f"Пароль не соответствует требованиям безопасности: {', '.join(results)}"
    else:
        return "Пароль соответствует всем требованиям безопасности"

def generate_password(): # функция генерации паролей
    quantity = is_digital(input('Количество паролей для генерации: '))
    length = is_digital(input('Длина одного пароля: '))
    chars = '' # строка, из которой формируется пароль

    while chars == '':
        if is_answer(input('Включать ли цифры 0123456789?(д/н) ')):
            chars += digits
        if is_answer(input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?(д/н) ')):
            chars += uppercase_letters
        if is_answer(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?(д/н) ')):
            chars += lowercase_letters
        if is_answer(input('Включать ли символы !#$%&*+-=?@^_?(д/н) ')):
            chars += punctuation
        if chars == '':
            print('-' * 61)
            print('Невозможно сгенерировать пароли. Выберите хотя бы одну опцию!')
            print('-' * 61)
            continue
        if chars != '' and is_answer(input('Исключать ли неоднозначные символы il1Lo0O?(д/н) ')):
            new_chars, chars = chars, ''
            for char in new_chars:
                if char not in similar:
                    chars += char
        else:
            print()
    print('-' * 61)
    print('Сгенерированные пароли:')
    for i in range(1, quantity + 1):
        password = sample(chars, length)
        print(f'{i}) {''.join(password)} - {is_safe(password)}')
    print('-' * 61)

digits = '0123456789'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'
similar = 'il1Lo0O'

again = True
print('Добро пожаловать в генератор паролей!')
while again:
    generate_password()
    again = is_answer(input('Сгенерировать ещё пароли?(д/н) '))
else:
    print('Спасибо, что воспользовались нашим генератором!')
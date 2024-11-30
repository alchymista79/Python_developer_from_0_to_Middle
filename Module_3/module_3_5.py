def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])

    if str_number.endswith('0'):
            str_number = str_number[:len(str_number)-1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

number = input('Введите целое число: ')
print(f'Произведение цифр числа {number} :', get_multiplied_digits(number))
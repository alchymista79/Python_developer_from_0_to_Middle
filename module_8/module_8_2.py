def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return (result, incorrect_data)


def calculate_average(numbers):
    res = 0
    try:
        c = len(numbers)
        try:
            d = personal_sum(numbers)
            res = d[0] / (c - d[1])
        except ZeroDivisionError:
            res = 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        res = None
    return res


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
import random

def get_key():
    list_key = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    key = random.choice(list_key)
    return key

n = get_key()
print('Ключ к шифру: ', n)
# подбираем пары чисел, кратные n (n должно делиться на сумму чисел этой пары без остатка, т.е. остаток от деления
# равен 0), само число n в список не входит (!)
num_pair_1 = list(range(1, n))
num_pair_2 = list(range(1, n))
pairs = []
code = ''

for i in num_pair_1:
    for j in num_pair_2:
        num_1 = i
        num_2 = j
        if num_1 >= num_2:
            continue
        else:
            result = n % (num_1 + num_2)
            if result == 0:
                pairs.append([num_1, num_2])
                code = code + str(num_1) + str(num_2)
print('Пары чисел', *pairs)
print('Введите пароль', code)
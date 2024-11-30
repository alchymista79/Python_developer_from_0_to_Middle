numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        numbers.remove(i)
for i in range(len(numbers)):
    h = 0 # счетчик числа делителей
    is_prime = numbers[i] # число из внового списка после исключения "1"
    for j in range(2, is_prime):
        if is_prime % j == 0:
            h = h + 1
            if h >= 1:
                break
    if h == 0:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print(primes)
print(not_primes)
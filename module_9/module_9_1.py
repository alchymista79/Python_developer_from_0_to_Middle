def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results.update({func.__name__: func(int_list)})
    return results


def min_(int_list):
    result = min(int_list)
    return result


def max_(int_list):
    result = max(int_list)
    return result


def len_(int_list):
    result = len(int_list)
    return result


def sum(int_list):
    result = 0
    for i in int_list:
        result += i
    return result


def sorted_(int_list):
    result = sorted(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

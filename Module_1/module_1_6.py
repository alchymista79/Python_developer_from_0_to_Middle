my_dict = {'me': 1979, 'mam': 1956, 'dad': 1954, 'wife': 1988}
print(my_dict)
print(my_dict['me'])
print(my_dict.get('son'))
my_dict.update({'son': 2008,
               'sister': 1978})
print(my_dict)
a = my_dict.pop('me')
print(a)
print(my_dict)

my_set = {2, 2, 4, 8, 5, 8, 'list', 'books', 'list', 4, 6, 'photo', 'list'}
print(my_set)
my_set.add(1)
my_set.add('dog')
print(my_set)
my_set.discard('list')
print(my_set)
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    str_num = 0
    byte_num = file.seek(0)
    for i in strings:
        file.write(i + '\n')
        str_num += 1
        key = (str_num, byte_num)
        string_positions[key] = i
        byte_num = file.tell()
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for i in result.items():
    print(i)
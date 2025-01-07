class WordsFinder:
    res = {}

    def __init__(self, *file_names):
        self.file_names = list(file_names)
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = ',.=!?;:'

        for i_file in self.file_names:
            words = []
            clear_line = ''
            with open(i_file, "r", encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    while line.find(' — ') != -1:
                        line = line.replace(' — ', " ")
                        continue
                    for char in line:
                        if not char in punctuation:
                            clear_line += char
                words = clear_line.split()
            all_words[i_file] = words
            self.res.clear()
        return all_words

    def find(self, word):
        for names, words in self.get_all_words().items():
            place = 0
            if word.lower() in words:
                place = words.index(word.lower()) + 1
                self.res[names] = place
        return self.res

    def count(self, word):
        for names, words in self.get_all_words().items():
            counter = 0
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[names] = counter
        return self.res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
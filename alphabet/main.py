# 3. Есть Алфавит, характеристиками которого являются:
# - Язык
# - Список букв
#
# Для Алфавита можно:
# - Напечатать все буквы алфавита
# - Посчитать количество букв

class Alphabet:
    language = ['English', 'Ukraine', 'Russia']
    list_literals = ['a', 'b', 'c', 'і', 'ї', 'є', 'я', 'э', 'ы', 'ъ']
    alphabet_len = None

    def write_alpha(self, lang):
        if lang == 'English':
            lang_alpha = self.list_literals[0:3]

        elif lang == 'Ukraine':
            lang_alpha = self.list_literals[3:7]
        elif lang == 'Russia':
            lang_alpha = self.list_literals[7:10]
        else:
            print("May be its something another.")
            return

        self.alphabet_len = len(lang_alpha)
        print(f'Consist of {len(lang_alpha)} literals : {lang_alpha}')


myLang = Alphabet()
print(f'Select one of {myLang.language} languages')
select_is = input()
myLang.write_alpha(select_is)
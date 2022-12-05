#Задача №111335. Статистика по файлу
#Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. Выведите три найденных числа в формате, приведенном в примере.
#Для экономии памяти читайте файл посимвольно, то есть не сохраняя целиком в памяти файл или отдельные его строки.

import string
letters = 0
words = 0
lines = 0
with open('text.txt', 'r') as tx:
    for i in tx.read():
        if i.isalpha():
            letters += 1
        elif i == ' ' or i == '\n':
            words += 1
        else:
            lines += 1

print(int(letters), 'letters')
print(int(words), 'words')
print(int(lines), 'lines')

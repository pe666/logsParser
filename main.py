error_counter = 0
data = None
next_line = False
filename = input('Введите название файла: ')
with open(filename, encoding='utf-8') as fh:
   data = fh.read()
with open(filename, 'wb') as fh:
    fh.write(data.encode('cp1251'))
with open(filename, 'r', encoding='cp1251') as f:
    for line in f.readlines():
        if next_line:
            with open('error_log.txt', 'a') as e:
                e.write(line)
                e.write('\n ---------------------------------------------------------------- \n')
                next_line = False
        if line.find('ERROR') != -1:
            error_counter += 1
            with open('error_log.txt', 'a') as e:
                e.write(line)
                next_line = True
print('Ошибок обнаружено:', error_counter)

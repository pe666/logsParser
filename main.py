import xlsxwriter
import re

error_counter = 0
data = None
next_line = False
filename = input('Введите название файла: ')
error_types = {}
time_position = []
try:
    with open(filename, encoding='utf-8') as fh:
        data = fh.read()
    with open(filename, 'wb') as fh:
        fh.write(data.encode('cp1251'))
except UnicodeDecodeError:
    pass
workbook = xlsxwriter.Workbook('ErrorTime.xlsx')
worksheet = workbook.add_worksheet()
with open(filename, 'r') as f:
    for line in f.readlines():
        if next_line:
            with open('error_log.txt', 'w') as e:
                e.write(line)
                e.write('\n ---------------------------------------------------------------- \n')
                next_line = False
        if line.find('ERROR') != -1:
            error_counter += 1
            with open('error_log.txt', 'a') as e:
                e.write(line)
                next_line = True
            res_str = line.partition(' - ')[2].replace('\n', '')
            date_time = re.match(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}', line)
            if res_str not in error_types.keys():
                error_types[res_str] = 1
                error_index = list(error_types.keys()).index(res_str)
                worksheet.write(0, error_index, res_str)
                time_position.append(1)
                worksheet.write(time_position[error_index], error_index, date_time[0])
                time_position[error_index] += 1
            else:
                error_index = list(error_types.keys()).index(res_str)
                error_types[res_str] += 1
                worksheet.write(time_position[error_index], error_index, date_time[0])
                time_position[error_index] += 1
workbook.close()
print('Ошибок обнаружено:', error_counter, '\n')
for key in error_types:
    print('Ошибка \"%s\" встречается %d раз' % (key, error_types[key]))

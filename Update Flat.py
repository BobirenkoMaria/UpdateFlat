from parse import parse
from Excel_work import *

is_file_exist = False

while is_file_exist != True:
    file_name = input('Введите название файла: ')
    is_file_exist = set_file_name(file_name)

print()
start_line = int(input('Начальная строка: '))
end_line = int(input('Конечная строка: ')) + 1
print()

info = parse(start_line, end_line)
input_to_worksheet(info, start_line, end_line)

input('Нажмите Enter, чтобы закрыть')

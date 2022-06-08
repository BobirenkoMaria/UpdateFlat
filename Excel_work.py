import openpyxl
import os.path

file_name_g = ''

def set_file_name(file_name):
    global file_name_g

    file_name = file_name.strip()
    if file_name[-5:] != '.xlsx':
        file_name += '.xlsx'

    file_name = fr'Files\{file_name}'

    is_file_exist = os.path.exists(file_name)

    if is_file_exist:
        file_name_g = file_name
    else:
        print("Такого файла не существует, проверьте правильность написания")

    return is_file_exist

def set_worksheet():
    global file_name_g

    wb = openpyxl.open(file_name_g)

    sheet = wb.active
    return sheet, wb


def input_to_worksheet(info, start_line, count):
    sheet, wb = set_worksheet()

    i = 0
    for line in range(start_line, count):
        sheet[line][7].value = int(info[i]['price'].replace(' ', ''))

        i+=1

    wb.save(file_name_g)
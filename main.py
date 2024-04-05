import my_lib.liba as lib
from datetime import date

path_root = '/home/alexey/dir_root/vipiski'         # корневой каталог
path_dist = '/home/alexey/dir_destination/'         # каталог назначения


#
file_list_full = lib.get_list_files(path_root)

# создаем архив всех файлов
today = str(date.today())
path_arx = today.replace('-', '/')
lib.creating_archive(file_list_full, path_dist + path_arx)

# удаление файлов
# lib.files_delete(file_list_full)



list_xml = lib.get_list_file_ext(file_list_full, '.xml')
list_html = lib.get_list_file_ext(file_list_full, '.htm')




# for file in file_list_full:
#     print(file)
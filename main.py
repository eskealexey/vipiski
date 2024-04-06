import my_lib.liba as lib
from datetime import date
import configparser


#получаем аргументы из конфигурационного файла
config = configparser.ConfigParser()
config.read('user.conf')
# print(config.sections())

path_root = config.get('DIR', 'r_vipiski')  # корневой каталог
path_dist = config.get('DIR', 'a_vipiski')  # каталог с архивами

password = config.get('FTP', 'pass')        # пароль к ФТП
ip = config.get('FTP', 'ip')                # ip адрес к ФТП
user_ftp = config.get('FTP', 'user')        # пользователь ФТП

print(path_root, path_dist )
print(password, ip, user_ftp)


file_list_full = lib.get_list_files(path_root)

# создаем архив всех файлов
today = str(date.today())
path_arx = today.replace('-', '/')
lib.creating_archive(file_list_full, path_dist + path_arx)

# удаление файлов
lib.files_delete(file_list_full)



list_xml = lib.get_list_file_ext(file_list_full, '.xml')
list_html = lib.get_list_file_ext(file_list_full, '.htm')




# for file in file_list_full:
#     print(file)
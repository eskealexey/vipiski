import my_lib.liba as lib
from datetime import date
import configparser


# получаем аргументы из конфигурационного файла
config = configparser.ConfigParser()
config.read('user.conf')
path_root = config.get('DIR', 'r_vipiski')          # корневой каталог
path_dist = config.get('DIR', 'a_vipiski')          # каталог с архивами
password = config.get('FTP', 'pass')                # пароль к ФТП
ip = config.get('FTP', 'ip')                        # ip адрес к ФТП
user_ftp = config.get('FTP', 'user')                # пользователь ФТП
ftp_vipiski = config.get('FTP_DIR', 'fDirVip')      # каталог с выпискамии рабочий (xml)
ftp_arxiv = config.get('FTP_DIR', 'fDirVypiski')    # каталог с файлами для архива (htm)


# Список всех файлов в каталоге и подкаталогах
file_list_full = lib.get_list_files(path_root)

# создаем архив всех файлов
today = str(date.today())
path_arx = today.replace('-', '/')
# lib.creating_archive(file_list_full, path_dist + path_arx)


# получаес список всех .xml файлов иоправляем на ФТП сервер
list_xml = lib.get_list_file_ext(file_list_full, '.xml')
for file_ in list_xml:
    subdir = file_[-61:-59]
    if subdir == '01':
        subdir = '1'
    elif subdir == '02':
        subdir = '2'
    elif subdir == '03':
        subdir = '3'
    elif subdir == '04':
        subdir = '4'
    elif subdir == '05':
        subdir = '5'
    elif subdir == '06':
        subdir = '6'
    elif subdir == '07':
        subdir = '7'
    elif subdir == '08':
        subdir = '8'
    elif subdir == '09':
        subdir = '9'
    # print(subdir)
    name_file = file_[-80:]
    xml_path = ftp_vipiski + subdir + '/'
    lib.ftp_upload(user_ftp, password, ip, file_, xml_path, name_file)


# получаем список всех .html файлов и отправляем на ФТП сервер
list_html = lib.get_list_file_ext(file_list_full, '.htm')
for file_ in list_html:
    subdir = file_[-61:-59]
    name_file = file_[-80:]
    html_path = ftp_arxiv + subdir + '/'
    lib.ftp_upload(user_ftp, password, ip, file_, html_path, name_file)


# удаление файлов
lib.files_delete(file_list_full)


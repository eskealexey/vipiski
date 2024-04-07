import my_lib.liba as lib
from datetime import date
import configparser





#получаем аргументы из конфигурационного файла
config = configparser.ConfigParser()
config.read('user.conf')
# print(config.sections())
path_root = config.get('DIR', 'r_vipiski')          # корневой каталог
path_dist = config.get('DIR', 'a_vipiski')          # каталог с архивами
password = config.get('FTP', 'pass')                # пароль к ФТП
ip = config.get('FTP', 'ip')                        # ip адрес к ФТП
user_ftp = config.get('FTP', 'user')                # пользователь ФТП
ftp_vipiski = config.get('FTP_DIR', 'fDirVip')      # каталог с выпискамии рабочий (xml)
ftp_arxiv = config.get('FTP_DIR', 'fDirVypiski')    # каталог с файлами для архива (htm)



# print(path_root, path_dist )
# print(password, ip, user_ftp)
# print(ftp_vipiski, ftp_arxiv)


file_list_full = lib.get_list_files(path_root)

# создаем архив всех файлов
today = str(date.today())
path_arx = today.replace('-', '/')
# lib.creating_archive(file_list_full, path_dist + path_arx)

# получаес список всех .xml файлов
# list_xml = lib.get_list_file_ext(file_list_full, '.xml')
# отправка на фтп
# lib.ftp_upload(user_ftp, password, ip, ftp_vipiski)


# получаес список всех .html файлов
list_html = lib.get_list_file_ext(file_list_full, '.htm')
for file_ in list_html:
    #OUT-600-INDPT-044-019-INNMB-2024-0-000176-OUTDPT-044-000-OUTNMB-2024-0004950.XML

    subdir = file_[-61:-59]
    name_file = file_[-80:]
    html_path = ftp_arxiv + subdir + '/'
    # print(subdir)
    # print(file_)
    # print(name_file)
    # print(html_path)

    lib.ftp_upload(user_ftp, password, ip, file_, html_path, name_file)


# удаление файлов
# lib.files_delete(file_list_full)






# for file in file_list_full:
#     print(file)
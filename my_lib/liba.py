import os
import zipfile
import zipfile as zip


# Функция получения списка файлов в каталоге и подкаталогах
def get_list_files(root_):
    list_ = []
    for root, dirs, files in os.walk(root_):
        for file in files:
            list_.append(os.path.join(root, file))
    return list_


# Получить список файлов по расширению
def get_list_file_ext(lst_, ext_):
    list_ext = []
    l = len(ext_)
    for file in lst_:
        str_ = str(file[-l:])
        if str_.lower() == str(ext_).lower():
            list_ext.append(file)
    return list_ext


def creating_archive(full, dist):
    dir_ = dist[:-2]
    name = dist[-2:]
    path_arx = dir_ + name + '.zip'
    if not os.path.isdir(dir_):
        os.makedirs(dir_)
    if os.path.isfile(path_arx):
        with zipfile.ZipFile(path_arx, mode='a') as archive:
            for f in full:
                archive.write(f)
    else:
        with zipfile.ZipFile(path_arx, mode='w') as archive:
            for f in full:
                archive.write(f)


    print(dist, dir_, name)





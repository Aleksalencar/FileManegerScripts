import os
import shutil
from configparser import ConfigParser
from file_maneger import file_manager


def copy(list,origin, destiny):
    for file in list:
        shutil.copy(origin+"\\"+file,destiny)
        print("Coping "+file+" to "+destiny)
    pass


def scan(folder):
    file_list = []
    files = os.scandir(folder)
    for file in files:
        if file.is_file():
            file_list.append(file.name)
            pass
        pass
    return file_list


def validation(source_files, destiny_files):
    copy_list = []
    list(source_files)
    list(destiny_files)
    for file in source_files:
        if not destiny_files.__contains__(file):
            copy_list.append(file)
        pass
    return copy_list


parser = ConfigParser()
parser.read('configurator\\configurations.ini')
source = parser.get('file_maneger', 'source')
destiny = parser.get('file_maneger', 'destiny')
source_files = scan(source)
destiny_files = scan(destiny)
copy_list = validation(source_files,destiny_files)
copy(copy_list, source, destiny)
file_manager.organize(destiny,False)

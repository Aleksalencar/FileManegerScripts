import os
import shutil

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)


def file_scan(path, filter_extensions):
    valid_files = []
    directory = os.scandir(path)
    for archive in directory:
        if archive.is_file():
            if filter_extensions is True:
                if is_extension_valid(archive.name):
                    valid_files.append(archive.name)
                    pass
            else:
                valid_files.append(archive.name)
                pass
            pass
        pass
    pass
    return valid_files


def is_extension_valid(archive):
    extensions = ['mkv', 'avi', 'mp4']
    archive = archive.split(".")
    if archive[-1] in extensions:
        return True
    return False


def dir_scan(path):
    folders = []
    directory = os.scandir(path)
    for archive in directory:
        if archive.is_dir():
            folders.append(archive.name)
            pass
        pass
    return folders


def move_file(path, file_list, dir_list):
    for file in file_list:
        dir = found_dir(file, dir_list)
        if dir is not None:
            move(path, file, dir)
        else:
            new_dir = make_dir(path, file)
            dir_list.append(new_dir)
            move(path, file, new_dir)
    pass


def found_dir(file, dir_list):
    file = file.replace('_', ' ')
    for dir in dir_list:
        if dir in file:
            return dir
        pass
    return None


def move(path, file, dir):
    source = path + "\\" + file
    destiny = path + "\\" + dir + "\\" + file
    print("moving " + file + " to " + dir)
    shutil.move(source, destiny)
    pass


def has_number(input_string):
    return any(char.isdigit() for char in input_string)
    pass


def assemble_path(dir_name):
    dir_name = dir_name.replace(".", " ")
    dir_name = dir_name.replace("_", " ")
    dir_name = dir_name.split()
    dir_name.pop()
    full_name = ''

    for i in range(len(dir_name)):
        if dir_name[i] == '-':
            continue
        if dir_name[i].startswith('[') or dir_name[i].endswith(']'):
            continue
        if has_number(dir_name[i]):
            break
        full_name = full_name + dir_name[i] + ' '
    full_name = full_name[:-1]
    return full_name


def make_dir(path, file):
    name = assemble_path(file)
    print("Criando " + path + "\\" + name)
    os.mkdir(path + "\\" + name)
    return name


def organize(path, filter):
    logging.debug('organizando %s' % (path))
    file_list = file_scan(path, filter)
    logging.debug(file_list)
    if len(file_list) == 0:
        print('Não há arquivos a ser organizados')
    else:
        dir_list = dir_scan(path)
        logging.debug(dir_list)
        move_file(path, file_list, dir_list)
    pass

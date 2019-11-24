import os
from configparser import ConfigParser

def is_extension_valid(archive):
    parser = ConfigParser()
    parser.read('file_maneger.ini')
    extensions = parser.get('file_maneger', 'extensions')
    archive = archive.split(".")
    print(archive[-1])
    print(extensions)
    ''''
    if archive[-1] in extensions:

        return True'''
    return False

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


def dir_scan(path):
    return None


def organize(path, filter):
    file_list = file_scan(path, filter)
    dir_list = dir_scan(path)

    pass

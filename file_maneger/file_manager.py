import os
import shutil
from configparser import ConfigParser


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
    print(valid_files)
    return valid_files


def is_extension_valid(archive):
    parser = ConfigParser()
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'file_maneger_settings.ini')
    parser.read(initfile)
    extensions = parser.get('settings', 'extensions')
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


def move_file(path,file_list, dir_list):
    for file in file_list:
        dir = found_dir(file,dir_list)
        print(dir)
        if dir is not None:
            move(path,file, dir)
        else:
            new_dir = make_dir(path,file)
            dir_list.append(new_dir)
            move(path, file, new_dir)
    pass

def found_dir(file, dir_list):
    for dir in dir_list:
        if dir in file:
            return dir
        pass
    return None


def move(path,file, dir):
    source = path+"\\"+file
    destiny = path+"\\"+dir+"\\"+file
    print("moving "+file+" to "+dir)
    shutil.move(source, destiny)
    pass


def make_dir(path,file):
    dir_name = file.replace("-", " ")
    dir_name = dir_name.replace("_", " ")
    dir_name = dir_name.replace(".", " ")
    dir_name = dir_name.split()
    dir_name = dir_name[0]
    print("Criando "+path+"\\"+dir_name)
    os.mkdir(path+"\\"+dir_name)
    return dir_name


def organize(path, filter):
    file_list = file_scan(path, filter)
    dir_list = dir_scan(path)
    move_file(path,file_list, dir_list)
    pass

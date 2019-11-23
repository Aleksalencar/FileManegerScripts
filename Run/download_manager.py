import os
import shutil
from configparser import ConfigParser

# Global
parser = ConfigParser()
parser.read('configurations.ini')
path = parser.get('paths', 'folder_path')
lim = parser.get('variables', 'word_limit')
dir = []
arcs = []


def separe_by_extesions (arq):  # verify if archive is a video
    extensions = parser.get('variables', 'extensions')
    arqExtension = arq.name.split(".")
    extension = arqExtension[- 1]
    if extension in extensions:
        return True
        pass
    return False


def archiveHasDir(archive, directory):  # verify if archive has a directory
    for sub in directory:
        if sub.lower() in archive.lower():
            return sub
            pass
    return None


def arqToDir(archive, directory):  # move archive to directory
    source = path + "\\" + archive
    destiny = path + "\\" + directory + "\\" + archive
    print("move " + archive + " to " + directory)
    shutil.move(source, destiny)
    pass


def newDir(vid):
    seriesName = vid.split("_"," ","-")
    name = seriesName[0]
    os.mkdir(name)
    dir.append(name)
    print("criando " + name)
    arqToDir(vid, name)
    pass


def separe_archives():
    os.chdir(path)
    directory = os.scandir()
    for archive in directory:  # Lista de diretorios
        if archive.is_dir():
            dir.append(archive.name)
            pass
        if separe_archives(archive):
            arcs.append(archive.name)
            pass
        pass
    pass
    for archive in arcs:  # cria
        arcDir = archiveHasDir(archive, dir)
        if arcDir is None:
            try:
                newDir(archive)
                pass
            except FileExistsError:
                print("FileExistsError")
                pass
            pass
        else:
            arqToDir(archive, arcDir)
            pass
        pass
    print("Organizing done in "+path)
    pass

# Main
separe_archives()
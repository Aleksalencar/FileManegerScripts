import os
import shutil
#Global
path = "D:\Downloads\Chrome"
lim = 6
dir = []
vids = []

def isVideo(arq): #verify if archive is a video
    videoExt = ["mkv", "avi", "mp4"]
    arqExtension = arq.name.split(".")
    extension = arqExtension[- 1]
    if extension in videoExt:
        return True
        pass
    return False


def archiveHasDir(archive, directory): #verify if archive has a directory
    for sub in directory:
        if sub.lower() in archive.name.lower():
            return sub
            pass
    return None


def arqToDir(archive, directory): # move archive to directory
    source = path+"\\"+archive.name
    destiny = path+"\\"+directory+"\\"+archive.name
    print("move "+archive.name+" to "+directory)
    shutil.move(source,destiny)
    pass

def newDir(vid):
    seriesName = vid.name.split("_")
    name = seriesName[0]
    os.mkdir(name)
    dir.append(name)
    print("criando " + name)
    arqToDir(vid, name)
    pass


#Main
os.chdir(path)
arqs = os.scandir()
for arq in arqs:  # Lista de diretorios
    if arq.is_dir():
        dir.append(arq.name)
        pass
    if isVideo(arq):
        vids.append(arq)
        pass
    pass
pass
for vid in vids: #cria 
    arcDir = archiveHasDir(vid, dir)
    if arcDir is None:
        try:
            newDir(vid)
            pass
        except FileExistsError:
            print("FileExistsError")
            pass
        pass
    else:
        arqToDir(vid,arcDir)
        pass
    pass
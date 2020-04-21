import file_manager
import PathManeger

if __name__ == '__main__':
    print('.: ORGANIZADOR DE ARQUIVOS :.')
    path_obj = PathManeger.PathManeger()
    paths = path_obj.read_paths()
    for i in range(len(paths)):
        print(i, ' - ', paths[i])
    opc = int(input())
    if 0 <= opc <= i:
        file_manager.organize(paths[opc], True)
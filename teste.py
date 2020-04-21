def dir_name_is_valid(dir_name):

    pass


def assemble_path(dir_name):
    dir_name = dir_name.replace(".", " ")
    dir_name = dir_name.replace("_", " ")
    dir_name = dir_name.split()
    dir_name.pop()
    full_name =''
    for name in dir_name:
        if name == '-':
            continue
        if name.startswith('[') or name.endswith(']'):
            continue
        if name.isnumeric():
            break
        full_name = full_name + name + ' '
    full_name = full_name[:-1]
    return full_name





    return dir_name
new_name = []
names = ['[Erai-raws] Boku no-Hero Academia 4th Season - 06 [1080p][Multiple Subtitle].mkv','Fruits_Basket_12_EA-Anbient.mkv','[OMDA]_Fruits_Basket_16_HQ [203CDEEC].avi','[Erai-raws] Kono Subarashii Sekai ni Shukufuku wo! - Kurenai Densetsu - Movie [1080p][Multiple Subtitle].mkv']
for name in names:
    new_name.append(assemble_path(name))
print(new_name)
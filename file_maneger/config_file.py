from configparser import ConfigParser
config = ConfigParser()

config['settings'] = {
    'folder_path': 'D:\Downloads\Chrome',
    'extensions': 'mkv, avi, mp4',
    'word_limit': '6',
    'top': '12344'
}

config['teste'] = {
    'teste':'teste123'
}

with open('./file_maneger_settings.ini', 'w') as f:
    config.write(f)

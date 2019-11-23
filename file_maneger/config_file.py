from configparser import ConfigParser

config = ConfigParser()


config['file_maneger'] = {
    'folder_path': 'D:\Downloads\Chrome',
    'extensions': 'mkv, avi, mp4',
    'word_limit': '6'
}

with open('configurations.ini', 'w') as f:
    config.write(f)

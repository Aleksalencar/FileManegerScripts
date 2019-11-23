import os
from configparser import ConfigParser

config = ConfigParser()

config['paths'] = {
    'folder_path': 'D:\Downloads\Chrome'
}
config['variables'] = {
    'extensions': 'mkv, avi, mp4',
    'word_limit': '6'
}

with open('configurations.ini', 'w') as f:
    config.write(f)

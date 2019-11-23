import os
from configparser import ConfigParser

config = ConfigParser()

config['paths'] = {
    'folder_path': 'D:\Downloads\Chrome'
}
config['variables'] = {
    'videoExt': "'mkv', 'avi', 'mp4'"
}

with open('configurations.ini', 'w') as f:
    config.write(f)

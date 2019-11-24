from configparser import ConfigParser
from tkinter import *
from configurator.configurator_boundary import Application

config = ConfigParser()


config['file_maneger'] = {
    'source':  'D:\Downloads\Chrome',
    'destiny': 'D:\Junior\Teste_DM'
}


root = Tk()
Application(root)
root.mainloop()
with open('configurations.ini', 'w') as f:
    config.write(f)

from file_maneger import file_manager
if __name__ == '__main__':
    path = "D:\Downloads\Chrome"
    print("organizando "+path)
    file_manager.organize(path,True)
    input()

def file_dir():
    import shutil
    file_or_dir = int(input('Скопировать 1. Папку. 2. Файл'))
    if file_or_dir == 1:
        dir_to_copy = input('Введите путь к папке, которую нажно скопировать ')
        dir_whi_copy = input('Введите путь к папке, которая будет создана ')
        shutil.copytree(dir_to_copy,dir_whi_copy)
    else:
        file_to_copy = input('Введите имя копируемого файла ')
        file_coping = input('Введите имя создаваемого файла ')
        shutil.copy(file_to_copy, file_coping)

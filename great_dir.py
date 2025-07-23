def dir_gr():
    dir_name = input('Введите название папки ')
    import os
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    else:
        print(f"Папка '{dir_name}' уже существует")
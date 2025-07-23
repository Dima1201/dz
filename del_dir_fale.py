def dir_fale():
    user_del = int(input('1. Удалить папку.\n2. Удалить файл.'))
    import os
    if user_del == 2:
        user_del_path = input('Введите путь к удаляемому файлу ')
        os.remove(user_del_path)
    else:
         user_del_dir = input('Введите путь к удаляемой папке ')
         import shutil
         shutil.rmtree(user_del_dir)
def charge():
    new_dir = input('Укажите путь к новой дирректории ')
    import os
    os.chdir(new_dir)


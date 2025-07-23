#Функция вызова главного меню
def main_menu():
    print('1. Создать папку.')
    print('2. Удалить папку/файлы')
    print('3. Копировать папку/файлы')
    print('4. Посмотр содержимого рабочей дирректории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей дирректории')
    print('12. Выход')

user_chouse = 0

while user_chouse != 12:
    main_menu()
    user_chouse = int(input())

    if user_chouse == 1:
        from great_dir import dir_gr
        dir_gr()

    if user_chouse == 2:
        from del_dir_fale import dir_fale
        dir_fale()

    if user_chouse == 3:
        from copy_file_dir import file_dir
        file_dir()

    if user_chouse == 4:
        import show_home
        show_home.home()

    if user_chouse == 5:
        import show_home
        show_home.home_dir()

    if user_chouse == 6:
        import show_home
        show_home.home_file()

    if user_chouse == 7:
        from os_info import info_os
        info_os()

    if user_chouse == 8:
        print('Создатель Дмитрий 6a6u4')

    if user_chouse == 9:
        from victor import vic
        vic()

    if user_chouse == 10:
        from bank import bank_check
        bank_check()

    if user_chouse == 11:
        from charge_dir import charge
        charge()
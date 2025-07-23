def bank_check():
    #Функция вывода главного меню
    def main():
        print('1. Пополнить счет')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

    user_chouse = 0
    chek = 0
    history_amount = {}
    while user_chouse != 4:
        main()
        user_chouse = int(input())
    #Пополнение
        if user_chouse== 1:
            user_replenishment = int(input('Сколько вы хотите пополнить?: '))
            chek = chek + user_replenishment
    #Покупка
        if user_chouse == 2:
            purchase_amount = int(input('Введите сумму покупки: '))
            if purchase_amount > chek:
                print('Недостотачно средств')
            else:
                user_amount = input('Введите название покупки: ')
                chek = chek - purchase_amount
                history_amount[user_amount] = purchase_amount
    #История покупок
        if user_chouse == 3:
            print(history_amount)
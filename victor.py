def vic():
    import random
    #Правильные ответы
    birthday = [{'Брэд Пит': '18.12.1963'},
                {'Виктор Цой': '21.06.1962'},
                {'Александр Пушкин': '26.05.1799'},
                {'Жанна Фриске': '8.07.1974'},
                {'Майкол Джексон': '29.08.1958'},
                {'Курт Кобейн': "20.02.1967"},
                {'Владимир Путин': '7.10.1952'},
                {'Андрей Макаревич': '11.12.1953'},
                {'Юрий Антонов': '19.02.1945'},
                {'Никола Тесла': '10.17.1856'}]

    #Переменная для запуска игры сначала
    start = 'Да'

    while start == 'Да':

        # Переменная счетчик вопросов
        ansver_count = 0

        # Правильные и неправильные ответы (счетчик)
        good_ansver = 0
        bad_ansver = 0

        #Вопросы (5шт)
        while ansver_count < 5:
            ansver_count += 1
            random_people = random.choice(birthday)

            #Получение ответа
            birthday_key_s = str(list(random_people.keys())[0])
            ansver_user = input('Укажите дату рождения '+ birthday_key_s + ': ')

            # Приведение ответа к словарю
            ansver = {birthday_key_s:ansver_user}

            #Проверка ответа и посчет
            if random_people != ansver:
                print('Ответ неверный')
                bad_ansver += 1
            else:
                print('Верно')
                good_ansver += 1

        print('Количество правильных ответов: ', good_ansver)
        print('Количество неправильных ответов: ', bad_ansver)
        print('Доля правильных ответов ', 100 / ansver_count * good_ansver)
        print('Доля неправильных ответов ', 100 / ansver_count * bad_ansver)

        good_ansver = 0
        bad_ansver = 0

        start = input('Начать игру сначала? ')
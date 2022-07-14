Pushkin_year = input('Введите год рождения А.С. Пушкина:')
if int(Pushkin_year) == 1799:
    Pushkin_day = input('Введите день и месяц рождения А.С. Пушкина в формате ДД-ММ:')
    if Pushkin_day == '06-06':
        print('Верно!')
    else:
        print('Неверный день')
else:
    print('Неверный год')

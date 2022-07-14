otvet_year = int(input('Введите год рождения А.С. Пушкина:'))
while(otvet_year != 1799):
    print('Неверно, попробуйте еще раз')
    otvet_year = int(input())
otvet_day = input('Введите день и месяц рождения А.С. Пушкина в формате ДД-ММ:')
while(otvet_day != '06-06'):
    print('Неверно, попробуйте еще раз')
    otvet_day = input()
print('Верно')
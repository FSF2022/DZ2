print('Викторина: "Хорошо ли вы знаете годы жизни известных людей?" ')
print('Необходимо вспомнить или угадать год рождения знаменитости, имя которой появится на экране. В конце викторины вас ждет результат')
r = 1
while r != 0:
    otvet = input('Год рождения  Эйнштейна: ')
    if otvet == '1879':
        s = 1
    else:
        s = 0
    otvet = input('Год рождения Ленина: ')
    if otvet == '1870':
        s += 1
    else:
        s += 0
    otvet = input('Год рождения Ньютона: ')
    if otvet == '1643':
        s += 1
    else:
        s += 0
    otvet = input('Год рождения Илона Маска: ')
    if otvet == '1971':
        s += 1
    else:
        s += 0
    otvet = input('Год рождения Билла Гейтса: ')
    if otvet == '1955':
        s += 1
    else:
        s += 0
    print('Ваш результат:')
    print(s, ' правильных ответа','(',s/5*100,'%), ', 5-s, ' неправильных ответа', '(',100-s/5*100, '%)')
    answer = input('Сыграем еще раз: Yes или No? ')
    if answer == 'Yes' or answer == 'yes' or answer == 'Y' or answer == 'y':
        r = 1
    else:
        r = 0
print('Всего хорошего, спасибо за участие')


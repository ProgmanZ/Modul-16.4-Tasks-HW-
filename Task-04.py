# Задача 4. Вечеринка

def count_guest(list_guests):
    count = 0
    for h in list_guests:
        count += 1
    return count


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:

    print(f'Сейчас на вечеринке {count_guest(guests)} человек:', guests)

    if count_guest(guests) == 0:
        print('Гостей нет. Может, имеет смысл закончить вечеринку?')

    action = input('Гость пришёл или ушёл? ')
    if action == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:
        name = input('Имя гостя: ')

        if action == 'пришёл' and 0 < count_guest(guests) < 6:
            if name == '':
                print('Ошибка... Вы забыли ввести имя.')
            else:
                print(f'Привет, {name}!')
                guests.append(name)

        elif action == 'ушёл':
            if name in guests:
                print(f'Пока, {name}!')
                guests.remove(name)
            else:
                print('Такого гостя нет.')

        elif count_guest(guests) >= 6:
            print(f'Прости, {name}, но мест нет.')

        elif action != 'пришёл' or action != 'ушёл':
            print('Ошибка...Принимаются команды "пришёл" или "ушёл".')
            print(f'Вы ввели: {action}\n')

        else:
            print('Произошло непредвиденное событие.')

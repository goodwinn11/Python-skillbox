guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    num_guest = len(guests)
    print(f'Сейчас на вечеринке {num_guest} человек: ', guests)
    command = input('Гость пришёл или ушёл? ')
    match command.lower():
        case 'пришёл':
            guest_name = input('Имя гостя: ')
            if num_guest > 5:
                print(f'Прости, {guest_name}, но мест нет')
            else:
                guests.append(guest_name)
        case 'ушёл':
            guest_name = input('Имя гостя: ')
            guests.remove(guest_name)
            print(f'Пока, {guest_name}')
        case 'пора спать':
            print('Вечеринка закончилась, все легли спать.')
            quit()


# TODO здесь писать код

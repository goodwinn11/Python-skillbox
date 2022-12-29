# TODO здесь писать код
num_people = int( input('Кол-во человек: '))
num_quit = int( input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {num_quit}-й человек')
current_list = list(range(1, num_people + 1))
current_num_index = 0
while len(current_list) > 1:
    print('\nТекущий круг людей:', current_list)
    print('Начало счета с номера', current_list[current_num_index])
    num_to_quit = current_num_index + num_quit - 1
    while num_to_quit > len(current_list) - 1:
        num_to_quit -= len(current_list)
    print('Выбывает человек под номером', current_list[num_to_quit])
    current_list.remove(current_list[num_to_quit])
    current_num_index = num_to_quit if num_to_quit < len(current_list) - 1 else num_to_quit - len(current_list)
print('Остался человек под номером', current_list[0])

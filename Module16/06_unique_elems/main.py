# TODO здесь писать код
first_list = []
second_list = []
for i in range(1, 4):
    number = int(input(f'Введите {i}-е число для первого списка: '))
    first_list.append(number)
for i in range(1, 8):
    number = int(input(f'Введите {i}-е число для второго списка: '))
    second_list.append(number)
final_list = first_list.copy()
final_list.extend(second_list)
for element in final_list:
    repetition = final_list.count(element)
    for i in range(repetition - 1):
        final_list.remove(element)
print('Первый список: ', first_list)
print('Второй список: ', second_list)
print('Новый первый список с уникальными элементами:', final_list)

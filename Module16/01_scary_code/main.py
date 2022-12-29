first_list = [1, 5, 3]
second_list = [1, 5, 1, 5]
third_list = [1, 3, 1, 5, 3, 3]
first_list.extend(second_list)
repeat_counter = first_list.count(5)
print('Кол-во цифр 5 при первом объединении:', repeat_counter)
for _ in range(first_list.count(5)):
    first_list.remove(5)
first_list.extend(third_list)
repeat_counter = first_list.count(3)
print('Кол-во цифр 3 при втором объединении:', repeat_counter)
print('Итоговый список: ', first_list)

# TODO переписать программу

# TODO здесь писать код
num_num = int(input('Кол-во чисел: '))
numbers = []
for _ in range(num_num):
    number = int(input('Число: '))
    numbers.append(number)
success_pairs = 0
i_number = 0
while i_number < num_num - success_pairs - 1:
    if numbers[i_number] == numbers[num_num - 1 - success_pairs]:
        success_pairs += 1
    else:
        success_pairs = 0
    i_number += 1
none_pairs = 1 if success_pairs == 0 else 0
numbers_needed = []
for i_number in range(num_num - 2 * success_pairs - 1 - none_pairs, -1, -1):
    numbers_needed.append(numbers[i_number])
print('Последовательность:', numbers)
print('Нужно приписать чисел: ', len(numbers_needed))
print('Сами числа:', numbers_needed)

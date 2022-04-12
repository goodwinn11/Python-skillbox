print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?
number = int(input("Введите номер билета: "))
first = number // 1000
last = number % 1000
first = first % 10 + (first  //10 % 10) + first // 100
last = last % 10 + (last // 10 % 10) + last // 100
if first == last:
  print("Номер билета счастливый")
else:
  print("Номер билета несчастливый")
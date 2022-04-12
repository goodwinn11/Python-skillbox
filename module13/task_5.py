print('Задача 5. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.
def digit_count(number):
  num_count = 0
  temp = number
  while temp > 0:
      num_count += 1
      temp //= 10
  return num_count

def mod_number(number):
  digits = digit_count(number)
  last_digit = number % 10
  first_digit = number // 10 ** (digits - 1)
  between_digits = number % 10 ** (digits - 1) // 10
  number = last_digit * 10 ** (digits - 1) + between_digits * 10 + first_digit
  return number
  
def digit_numbers(number, required_digits, count):
  if digit_count(number) < required_digits:
    print(f"В числе меньше {required_digits} цифр")
  
  else:
    modified_number = mod_number(number)
    return modified_number
    
def num_input(count):
  number = int(input(f"Введите {count} число: "))
  return number

first_n = num_input(1)
first_n_mod = digit_numbers(first_n, 3, 1)
if first_n_mod != None:
  print('Изменённое первое число:', first_n_mod)
second_n = num_input(2)
second_n_mod = digit_numbers(second_n, 4, 2)
if second_n_mod != None:
  print('Изменённое второе число:', second_n_mod)
if first_n_mod != None and second_n_mod != None:
  print('\nСумма чисел:', first_n_mod + second_n_mod)
print('Задача 1. Кубы чисел')

# Любителю математики Паше снова стало мало распечатанных табличек,
# включая последнюю со степенями двойки.
# Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!

# Напишите программу,
# которая возводит в третью степень каждое число от 1 до N
# и выводит результат на экран.
number = int(input("Введите до какого числа считать: "))
i = 1
while i <= number:
  print("Число", i, "в степени 3 равно", i ** 3)
  i += 1
print('Задача 4. Число наоборот')

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
# 
# Введите число: 1000
# Число наоборот: 0001
# 
# Введите число: 0
# Программа завершена!
# 
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
# 
# Введите число: 1230
# Число наоборот: 321
# 
# Кстати, нули, которые мы убрали, называются ведущими.
def main():
  number = input("Введите число: ")
  if number == '0':
    print("Программа завершена!")
  else:
    rotate(number)

def rotate(number):
  
  rotated = ""
  number = int(number)
  while number % 10 == 0:
    number /= 10
  number = str(int(number))
  for letter in number:
    rotated = letter + rotated
  print("Число наоборот:", rotated)
  main()

main()

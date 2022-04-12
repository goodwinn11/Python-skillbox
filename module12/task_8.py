print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def nod(number_1, number_2):
  max_nod = 1
  for i in range(1, min(number_1, number_2)+1):
    if number_1 % i == 0 and number_2 % i == 0 and i > max_nod:
      max_nod = i
  print("Наибольший общий делитель равен: ", max_nod)

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
nod(number_1, number_2)

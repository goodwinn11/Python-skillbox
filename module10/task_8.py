print('Задача 8. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######
height = int(input("Введите высоту пирамидки: "))
for row in range (height):
  for col in range ( 2 * height):
    if (col <= height + row) and (col >= height - row):
      print("#", end = "")
    else:
      print(" ", end = "")
    
  print()

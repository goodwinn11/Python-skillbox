print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.
number = int(input("Введите количество учеников в классе: "))
three = 0
four = 0
five = 0
for i in range(1, number + 1):
  mark = int(input("Введите оценку "+str(i)+" ученика: "))
  if mark == 3:
    three += 1
  elif mark == 4:
    four += 1
  else:
    five += 1
if three >= four and three >= five :
  print ("Сегодня больше троечников")
elif four >= five and four >= three:
  print ("Сегодня больше хорошистов")
else:
  print ("Сегодня больше отличников")
print('Задача 1. Календарь')

# Мы продолжаем разрабатывать удобный календарь для смартфона.
# Функцию определения високосного года мы добавили,
# но забыли ещё много разных очевидных вещей.
# 
# Напишите программу,
# которая принимает от пользователя день недели в виде строки и выводит его номер на экран.
# 
# Пример:
# Введите день недели: вторник
# Номер дня недели: 2
dayName = input("Введите день недели: ")
dayNumber = 0
if dayName == "Понедельник" or dayName == "понедельник":
  dayNumber = 1
elif dayName == "Вторник" or dayName == "вторник":
  dayNumber = 2
elif dayName == "Среда" or dayName == "среда":
  dayNumber = 3
elif dayName == "Четверг" or dayName == "четверг":
  dayNumber = 4
elif dayName == "Пятница" or dayName == "пятница":
  dayNumber = 5
elif dayName == "Суббота" or dayName == "суббота":
  dayNumber = 6
elif dayName == "Воскресенье" or dayName == "воскресенье":
  dayNumber = 7
if dayNumber == 0:
  print("День недели введен неверно")
else:
  print("Номер дня недели:", dayNumber)
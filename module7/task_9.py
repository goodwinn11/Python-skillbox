print('Задача 9. ...Теперь можно посчитать и свою')

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# 
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.

previous = 0
rost = True
for i in range (1, 11):
  salary = int(input("Введите зарплату за "+str(i)+" месяц: "))
  if salary < previous:
    rost = False
    print ("Зарплата не увеличивается каждый месяц")
    break
  previous = salary
if rost:
  print("Зарплата увеличивается каждый месяц")

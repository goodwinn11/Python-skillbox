print('Задача 10. Поменять местами: не всё так просто! (необязательная, повышенной сложности)')

# Мы умеем менять местами строковые переменные и знаем,
# что в переменных, кроме строк, можно хранить и числа.
# Напишите программу, которая меняла бы значения двух переменных местами,
# но без использования третьей переменной и без использования  синтаксического сахара,
# который мы разбирали, а именно — без конструкции a,b = b,a.
# В переменные будут вводиться только числа.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
b += a 
a = b - a
b -=  a
print(a, b)

# Изменять, удалять, менять местами 10, 11 строку, первый и второй print нельзя.
# Но между 12-й и 14-й строчкой можно вставлять сколько угодно строк кода, не трогая последний принт.

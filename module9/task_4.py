print('Задача 4. Театр')

# Планируется построить театр под открытым небом,
# но для начала нужно хотя бы примерно понять сколько должно быть рядов,
# сидений в них и какое лучше сделать расстояние между рядами.
#
# Напишите программу,
# которая получает на вход кол-во рядов, сидений и свободных метров между рядами,
# а затем выводит примерный макет театра на экран.

# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
rows = int(input("Введите количество рядов: "))
places = int(input("Введите количество сидений в ряду: "))
distance = int(input("Введите расстояние между рядами: "))
for i in range(rows):
  rowLayout = places * "=" + distance * "*" + places * "=" 
  print(rowLayout)
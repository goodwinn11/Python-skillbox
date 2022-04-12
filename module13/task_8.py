print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709
def grade(number, grade):
  graded = number
  i = 1
  while i < grade:
    graded *= number
    i += 1
  #print("graded", graded)
  if grade == 0:
    graded = 1
  return graded

def factor(number):
  fact = 1
  for i in range (1, number + 1):
    fact *= i
  return fact

precision = float(input("Введите точность: "))
x = int(input("Введите х: "))
row = 0
prev_row = 1
n = 0

while abs(row - prev_row) >= precision:
  prev_row = row
  row = prev_row + grade(-1, n) * grade(x, (2 * n)) / factor((2 * n))
  n += 1
print("Сумма ряда =", row)

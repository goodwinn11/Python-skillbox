print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 
x = int(input("Введите число х: "))
numerator = 1
denominator = 1
for i in range(1,7):
  if x == 2 ** i:
    denominator = 0;
    break
  numerator *= (x - 2 ** i + 1)
  denominator *= (x - 2 ** i)
if denominator != 0:
  print("Результат выражения равен:", numerator / denominator)
else:
  print("Деление на ноль!")
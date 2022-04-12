print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 
summ = 0
factorial = 1
number = int(input("Введите число: "))
for i in range(1, number + 1):
  for j in range(1, i + 1):
    factorial *= j
  summ += factorial
  factorial = 1
print("Сумма факториалов равна", summ)
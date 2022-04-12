print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
number = int(input("Введите число: "))
text = ""
for row in range (number):
  for i in range (2 * number):
    if i <= row:
      text = text + str( number - i)
    elif (2 * number - i - 1) <= row:
      text = text + str( i + 1 - number)
    else:
      text = text + "."
  print(text)
  text = ""    


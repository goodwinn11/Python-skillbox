print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29
height = int(input("Введите высоту пирамидки: "))
number = 1
text = ""
text_number = ""
for row in range (1, height+1):
  for i in range(row):
    text_number = str(number)
    text_number = (4 - len(text_number)) * " " + text_number
    text = text + text_number
    number += 2
  text = (2 * height - len(text) // 2) * " " + text + (2 * height - len(text) // 2) * " "
  print (text)
  text = ""
    
print()

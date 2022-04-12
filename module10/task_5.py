print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.
text = input("Введите последовательность чисел через пробел: ")
text = text + " "
text_number = ""
count = 0

for symbol in text:
  if symbol != " ":
    text_number = text_number + symbol
  else:
    number = int(text_number)
    simple = True
    for i in range(2, number):
      if number % i == 0:
        simple = False
        break
    if simple:
      count +=1
    text_number = ""
print("Простых чисел в последовательности", count)

print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
text = input("Введите последовательность чисел через пробел: ")
text = text + " "
text_number = ""
count = 0
summ = 0
max_sum = 0
max_num = ""
for symbol in text:
  if symbol != " ":
    text_number = text_number + symbol
  else:
    number = int(text_number)
    if number > 0:
      for symbol in text_number:
        summ += int(symbol)
        if summ > max_sum:
          max_sum = summ
          max_num = text_number
      summ = 0
    text_number = ""
print(f"Максимальная сумма цифр {max_sum} в числе {max_num}")


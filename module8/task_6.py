print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.
size = int(input("Введите размер письма: "))
lay = 0
while size > 12:
  size //= 2
  lay += 2
print("Письмо необходимо сложить", lay, "раз")
print('Задача 4. Калькулятор скидки')

# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные комнаты.
# Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть. 
# Вот для одного из таких магазинов он и написал калькулятор скидки, 
# чтобы проще ориентироваться в ценах.
 
# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека. 
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). 
# В конце вывести итоговую сумму на экран.
first_price = int(input("Введите стоимость первого товара "))
second_price = int(input("Введите стоимость второго товара "))
third_price = int(input("Введите стоимость третьего товара "))
if first_price + second_price + third_price > 10000:
  sum = (first_price + second_price + third_price) * 0.9
else:
  sum = (first_price + second_price + third_price)
print("Cтоимость покупки составляет", sum)

print('Задача 9. В обратном порядке')

# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.
number = int(input("Введите четырехзначное число: "))
first = number // 1000
second = (number // 100) % 10
third = ((number // 10) % 100) % 10
fourth = number % 10
print (fourth*1000+third*100+second*10+first)
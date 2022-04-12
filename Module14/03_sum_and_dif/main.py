def summ(number):
    summ = 0
    for i in number:
        summ += int(i)
    return summ

def digits(number):
    digits = 0
    for i in number:
        digits += 1
    return digits

number = input("Введите число: ")
print("Сумма цифр числа:", summ(number))
print("Количество цифр в числе:", digits(number))
print("Разность суммы и кол-ва цифр:", summ(number) - digits(number))

# зачет!

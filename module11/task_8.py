print('Задача 8. Часы')

# С начала суток часовая стрелка повернулась на угол в α градусов.
# Определите на какой угол повернулась минутная стрелка с начала последнего часа. 
# Входные и выходные данные — действительные числа.
# 
# При решении этой задачи нельзя пользоваться условными операторами и циклами.
angle = int (input("Введите на какой угол повернулась часовая стрелка с начала суток "))
angle %=  30
minute_angle = int(angle / 30 * 360)
print(f"Минутная стрелка повернулась на {minute_angle} градусов")


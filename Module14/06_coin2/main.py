import math
def presense(x, y, r):
    distance = math.sqrt(x ** 2 + y ** 2) / 2
    if distance <= r:
        return True
    else:
        return False

x = float(input("Введите координату х: "))
y = float(input("Введите координату у: "))
r = float(input("Введите радиус: "))
if presense(x, y, r) == True:
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")

# зачет!

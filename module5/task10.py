print('Задача 10. Почта')

# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед,
# а в 10:00 и 18:00 приезжают машины с посылками,
# и тогда все сотрудники на два часа заняты их разгрузкой.
# Во время обеда, разумеется, посылки никто не выдаёт,
# как и в моменты, когда разгружаются машины.

# Напишите программу,
# которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.

# Решите задание двумя способами:

# первый — при выполнении условия выводится сообщение:
# «Можно получить посылку»,

# второй —  при выполнении условия выводится сообщение:
# «Посылку получить нельзя».
visit_time = int(input("Введите время визита "))
if (visit_time >= 8 and visit_time < 10) or (visit_time >= 12 and visit_time < 14) or (visit_time >= 15 and visit_time < 18) or (visit_time >= 20 and visit_time < 22):
  print("Можно получить посылку")

if (visit_time< 8) or (visit_time >= 10 and visit_time < 12) or (visit_time >= 14 and visit_time < 15) or (visit_time >= 18 and visit_time < 20) or (visit_time >= 22) :
    print("Посылку получить нельзя")
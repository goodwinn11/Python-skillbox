shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
detail = input('Название детали: ')
num_detail = 0
total_cost = 0
for current in shop:
    if current[0] == detail:
        num_detail += 1
        total_cost += current[1]
print('Кол-во деталей —', num_detail)
print('Общая стоимость —', total_cost)

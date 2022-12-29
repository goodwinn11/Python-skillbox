# TODO здесь писать код
num_roller = int(input('Кол-во коньков: '))
roller = []
for i in range(1, num_roller + 1):
    size = int(input(f'Размер {i}-й пары: '))
    roller.append(size)
people = []
num_people = int(input('\nКол-во людей: '))
for i in range(1, num_people + 1):
    size = int(input(f'Размер ноги {i}-го человека: '))
    people.append(size)
roller.sort()
people.sort()
num_success = 0
for people_size in people:
    for roller_size in roller:
        if roller_size >= people_size:
            num_success += 1
            roller.remove(roller_size)
            continue
print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {num_success}')

# TODO здесь писать код
number_friends = int(input('Кол-во друзей: '))
friends = []
for _ in range(number_friends):
    friends.append(0)
number_papers = int(input('Долговых расписок: '))
for i_paper in range (number_papers):
    print(f'{i_paper + 1}-я расписка\n')
    borrower = int(input('Кому: '))
    creditor = int(input('От кого:  '))
    amount = int(input('Сколько:  '))
    friends[borrower - 1] -= amount
    friends[creditor - 1] += amount
print('Баланс друзей:')
for i in range(number_friends):
    print(f'{i+1}: {friends[i]}')


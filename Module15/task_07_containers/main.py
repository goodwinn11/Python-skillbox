
def check():
    weight = input("Введите вес контейнера: ")
    weight = float(weight)
    if 0 < weight < 200 and weight % 1 == 0:
        weight = int(weight)
        return weight
    else:
        print("Ошибка ввода! ")
        check()

def main():
    number = int(input("Количество контейнеров: "))
    cont_list = []
    for i in range(number):
        cont_list.append(check())
    new_cont = int(input("Введите вес нового контейнера: "))
    found = False
    for i in range(number):
        if not found and int(cont_list[i]) < new_cont:
            position = i + 1
            found = True
    print("Номер, куда встанет новый контейнер:", position)



if __name__ == '__main__':
    main()

# зачет!

def main():
    number = int(input("Кол-во видеокарт: "))
    model = []
    latest_model = 0
    for i in range(number):
        model.append(int(input("Видеокарта: ")))
    print("\nCтарый список видеокарт:", model)
    for i in range(number):
        if model[i] > latest_model:
            latest_model = model[i]
    deleted = 0
    for i in range(number):
        if model[i - deleted] == latest_model:
            model.pop(i - deleted)
            deleted += 1
    print("Новый список видеокарт:", model)


if __name__ == '__main__':
    main()

# зачет!

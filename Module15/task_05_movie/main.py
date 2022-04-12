def main():
    films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
             'Леон', 'Богемская рапсодия', 'Город грехов',
             'Мементо', 'Отступники', 'Деревня']
    number = int(input("Сколько фильмов хотите добавить? "))
    favorite = []
    for i in range(number):
        film_name = input("Введите название фильма: ")
        found = False
        for j in range(len(films)):
            if films[j].lower() == film_name.lower():
                favorite.append(films[j])
                found = True
        if not found:
            print(f"Ошибка: фильма {film_name} у нас нет :(")
    print("Ваш список любимых фильмов:", favorite)


if __name__ == '__main__':
    main()

# согласен
# зачет!

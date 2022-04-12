def main():
    elements = []
    size = int(input("Введите размер списка: "))
    for i in range(size):
        elements.append(int(input(f"Введите {i + 1} элемент списка: ")))
    shift = int(input("Сдвиг: "))
    pass
    new_elements = []
    for i in range(size):
        new_elements.append(elements[i - shift])
    print("Сдвинутый список:", new_elements)
    pass


if __name__ == '__main__':
    main()

# зачет!

def main():
    size = int(input("Введите размер списка: "))
    elements = []
    for i in range(size):
        elements.append(int(input(f"Введите {i + 1} элемент списка: ")))
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(elements)):
            if (elements[i] < elements[i - 1]) and (i != 0):
                elements[i], elements[i - 1] = elements[i - 1], elements[i]
                sorted = False
    print("Отсортированный список: ", elements)


if __name__ == '__main__':
    main()

# зачет!

def main():
    n = int(input("Введите число: "))
    numbers = []
    for i in range(1, n + 1, 2):
        numbers.append(i)
    print(f"Список из нечётных чисел от 1 до N:", numbers)


if __name__ == '__main__':
    main()

# зачет!

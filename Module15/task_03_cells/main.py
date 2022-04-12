def main():
    number_cells = int(input("Кол-во клеток: "))
    effectiveness = []
    for i in range(number_cells):
        effectiveness.append(int(input(f"Эффективность {i + 1} клетки: ")))
    count = 1
    print("\nНеподходящие значения:", end=" ")
    for i in range(number_cells):
        if effectiveness[i] < count:
            print(effectiveness[i], end=" ")
        count += 1



if __name__ == '__main__':
    main()

# зачет!

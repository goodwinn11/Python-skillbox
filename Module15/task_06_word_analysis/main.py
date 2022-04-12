def main():
    word = input("Введите слово: ")
    word = list(word)
    count = 0
    for i in range(len(word)):
        unique = True
        for j in range(len(word)):
            if word[j] == word[i] and j != i:
                unique = False
        if unique:
            count += 1
    print("Кол-во уникальных букв:", count)


if __name__ == '__main__':
    main()

# зачет!

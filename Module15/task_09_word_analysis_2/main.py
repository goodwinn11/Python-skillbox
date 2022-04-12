def main():
    word = input("Введите слово: ")
    word = list(word)
    palindrome = True
    for i in range(int(len(word) // 2)):
        if word[i] != word[len(word) - 1 - i]:
            first = word[i]
            last = word[len(word) - 1]
            palindrome = False
    if palindrome:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")


if __name__ == '__main__':
    main()

# зачет!

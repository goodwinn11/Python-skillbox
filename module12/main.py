print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random
def rock_paper_scissors():
  comp_choise = random.randint(1, 3)
  #1-камень 2- ножницы 3 - бумага
  user_choise = input("Камень, ножницы или бумага? ")
  if user_choise.lower() == "камень" and comp_choise == 1:
    print("У меня тоже камень, ничья")
    mainMenu()
  elif user_choise.lower() == "камень" and comp_choise == 2:
    print("У меня ножницы, ты победил")
    mainMenu()
  elif user_choise.lower() == "камень" and comp_choise == 3:
    print("У меня бумага, я победил")
    mainMenu()
  elif user_choise.lower() == "ножницы" and comp_choise == 1:
    print("А у меня камень, я победил")
    mainMenu()
  elif user_choise.lower() == "ножницы" and comp_choise == 2:
    print("И у меня ножницы, ничья")
    mainMenu()
  elif user_choise.lower() == "ножницы" and comp_choise == 3:
    print("А у меня бумага, ты победил")
    mainMenu()
  elif user_choise.lower() == "бумага" and comp_choise == 1:
    print("А у меня камень, ты победил")
    mainMenu()
  elif user_choise.lower() == "бумага" and comp_choise == 2:
    print("А у меня ножницы, я победил")
    mainMenu()
  elif user_choise.lower() == "бумага" and comp_choise == 3:
    print("И у меня бумага, ничья")
    mainMenu()
  else:
    print("Неправльный ввод, повторите попытку")
    rock_paper_scissors()
    
def guess_the_number():
  user_number = int(input("Введите число: "))
  comp_number = random.randint(0, 9)
  if user_number == comp_number:
    print(f"У меня тоже {comp_number}, угадал")
    mainMenu()
  else:
    print(f"А у меня {comp_number}, не угадал")
    guess_the_number()

def mainMenu():
  game = int(input("Введите номер игры (1- камень, ножницы, бумага; 2 - угадай число) "))
  if game == 1:
    rock_paper_scissors()
  elif game == 2:
    guess_the_number()
  else:
    print("Необходимо выбрать 1 или 2")
    mainMenu()
mainMenu()

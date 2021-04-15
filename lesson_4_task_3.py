# 5)	Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести.
#  Функция возвращает введённое число.
# * Теперь далее для других задач с числами, вы можете пользоваться этой функцией, а не простым input!

def enter_number (x = input("Enter the number: ")):
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            x = input("Enter the number: ")





# 6)	Пишем функцию, которая попросит пользователя ввести слово (строка из буквенных символов без пробелов в середине,
# а вначале и в конце пробелы могут быть).
# Пока он не введёт правильно, просите его ввести. Функция возвращает введённое слово.

def enter_word (word = input("Enter word: ")):
    word_wihout_spases = word.strip()
    while  word_wihout_spases.count(" ") != 0:
        print(word)
        if word_wihout_spases.count(" ") == 0:
            print(word)
            return word
        elif word_wihout_spases.count(" ") != 0:
            word = input("Enter word without spases inside: ")
        # for i in word:
        #     if int(i)/1 == int(i):
        #         print(int(word))
        #         word = input("Enter word without numbers: ")
        #     else:
        #         return word


if __name__ == "__main__":
    # print(enter_number())
    print(enter_word())

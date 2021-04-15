# Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
#
# 1-е число – сколько строк будет в песне. По умолчанию 3
# 2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
# 3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!». По умолчанию 0


# впевнений що можна це зробити набагато простіше, навіть трохи сумно, що в голову прийшло лише таке рішення
# з хорошого - це працює
def song (strings = 3, words_la = 3, ending = 0):
    la = "la"
    divider = "-"
    if words_la <= 0 or strings <= 0:
        return None
    elif words_la <= 1:
        if strings <=1:
            if ending == 0:
                return la * words_la + "."
            elif ending == 1:
                return la * words_la + "!"
        elif strings > 1:
            if ending == 0:
                return (la * words_la + "\n") * (strings - 1) + la * words_la + "."
            elif ending == 1:
                return (la * words_la + "\n") * (strings - 1) + la * words_la + "!"
    elif words_la > 1:
        if strings <=1:
            if ending == 0:
                return (la + divider) * (words_la - 1) + la + "."
            elif ending == 1:
                return (la + divider) * (words_la - 1) + la + "!"
        elif strings > 1:
            if ending == 0:
                return ((la + divider) * (words_la - 1) + la + "\n") * (strings - 1) + (la + divider) * (words_la - 1) + la + "."
            elif ending == 1:
                return ((la + divider) * (words_la - 1) + la + "\n") * (strings - 1) + (la + divider) * (words_la - 1) + la + "!"
        elif words_la <= 0 and strings <=0:
            return None



if __name__ == "__main__":
    print(song(3,3,0))



#•	Посчитайте сколько слов в тексте

x = "We are not what, we should be!\nWe are not what we, need to be.\nBut at least we are not what we used to be\n(Football Coach)"
# print(x.split("\n"))
# print(x.split(" "))

print(len(x.split(" ")) + len(x.split("\n")) - 1)


# •	Удалите знаки препинания в списке слов (пройдитесь циклом все слова и удалите методом strip знаки препинания)

some_list = ["Word", ",,fish", "sky,", "sun." ]

for element in some_list:
    while element.find(",") != -1:
        print(element)
        if element.find(",") == -1:
           continue
        else:
            element.strip(",")  # якщо я правильно зрозумів, то елемент ,,fish сюди заходить, але чомусь не видаляються коми
print(some_list)



# •	Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)

list_with_names = ["Mike", "John", "Annet", "Bob", "John", "Bob", "Bob"]


print(sorted(list_with_names))

# •	Посчитать, сколько раз встречается каждое слово.
# (Подсказка: создавать словарь, где ключи — это слова из текста,
# а в значениях подсчитываем количество «встречаний» этого слова)

list_with_names = ["Mike", "John", "Annet", "Bob", "John", "Bob", "Bob", "mike", "bob"]

repeat_counter ={}

for name in list_with_names:
    if name not in repeat_counter:
        repeat_counter[name] = 1
    elif name in repeat_counter:
        repeat_counter[name] += 1


print(repeat_counter)

# •	Слова с большой буквы и с маленькой это все равно одно и тоже слово

for name in list_with_names:
    if name.title() not in repeat_counter:
        repeat_counter[name] = 1
    elif name.title() != name:
        repeat_counter[name.title()] += 1
    elif name in repeat_counter:
        repeat_counter[name] += 1

print(repeat_counter)

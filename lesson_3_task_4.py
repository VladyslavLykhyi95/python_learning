import time
# У вас есть список чисел.
# 1.	Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым


some_list = [1, 5, 131, 3145, 322]

while len(some_list) != 0:
    for i in some_list:
        some_list.remove(i)
        print(some_list)

# 2.	** Как сделать это же задание со строкой:
# напишите цикл, который выводит на экран и «удаляет» первый символ строки, пока она не станет пустой?

some_string = "Some text"
# # some_string = list(some_string)
# some_string.replace(some_string[0], "")
# print(some_string[0])
# print(some_string)

while len(some_string) > 0:
    some_string = list(some_string)
    some_string.pop(0)
    some_string = "".join(some_string)
    print(some_string)


print(some_string)

# 3.	Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого,
# пока он не останется пустым.

some_list = [1, 5, 131, 3145, 322]

while len(some_list) != 0:
    for i in some_list:
        i = min(some_list)
        print(i)
        some_list.remove(i)
# 4.	** Дана последовательность натуральных ненулевых чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

some_sequence = [1, 3, 3, 3, 3, 2, 2, 3, 1, 0]

counter = {}

for index in range(len(some_sequence)):
    # print(index)
    if some_sequence[index] == some_sequence[index-1]:
        if some_sequence[index] not in counter:
            counter[some_sequence[index]] = 2
        else:
            counter[some_sequence[index]] += 1
        # for number in some_sequence:
        #     if number not in counter:
        #         counter[index] = 2
        #         print(counter)
        #     elif number in counter:
        #         counter[index] = counter[index] + 1
    # elif some_sequence[index] != some_sequence[index-1]:
    #     for number in some_sequence:
    #         counter[number] = -1





print(max(counter.values()))
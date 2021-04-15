from math import acos, pi

# 1)	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
# если год високосный, и False иначе.

def is_year_leap (year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


# 2)	Функция принимает три числа a, b, c.
#     Функция должна определить, существует ли треугольник с такими сторонами.
#     Если треугольник существует, вернёт True, иначе False.

def triangle (a, b, c): #теорема косинусів
    try:
        angle_1 = acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
        angle_2 = acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
        angle_3 = acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
        if angle_1 + angle_2 + angle_3 == pi:
            return True
        else:
            return False
    except ValueError:
        return False

# print(triangle(1,4,4))

def triangle_type (a, b, c):
    if triangle(a,b,c) == True:
        if a == b and b == c and c == a:
            return "Equilateral triangle"
        elif a == b or b == c or c == a:
            return "Isosceles triangle"
        elif a != b and b != c and c != a:
            return "Versatile triangle"
    elif triangle(a,b,c) == False:
        return "Not a triangle"

    # try:
    #     angle_1 = acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    #     angle_2 = acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    #     angle_3 = acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    #     print(angle_1 + angle_3 + angle_2)
    #     if angle_1 + angle_2 + angle_3 == pi:
    #         if angle_1 == angle_2 == angle_3:
    #             return print("Equilateral triangle")
    #         elif angle_1 == angle_2 or angle_2 == angle_3 or angle_3 == angle_1:
    #             return print("Isosceles triangle")
    #         elif angle_1 != angle_2 or angle_2 != angle_3 or angle_3 != angle_1: # можливо тут було достатньо лише else?
    #             return print("Versatile triangle")
    #     else:
    #         return print("Not a triangle")
    # except ValueError:
    #     return print("Not a triangle")




# 4)	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точками с координатами (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя
# (перед запуском функции, не внутри функции) и выведите результат работы этой функции.


cordinates = {"x1": int(input("Enter value for x1: ")), "y1": int(input("Enter value for y1: ")),
              "x2": int(input("Enter value for x2: ")), "y2": int(input("Enter value for y2: "))}
def distance (cordinates):
    distance = ((cordinates["x2"] - cordinates["x1"]) ** 2 + (cordinates["y2"] - cordinates["y1"]) ** 2) ** 0.5
    return distance


if __name__ == "__main__":
    print(is_year_leap(700))
    print(triangle_type(3, 3, 3))
    print(distance(cordinates))

# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def Input_Number(num):
    xy = ["X", "Y"]
    coord = []
    for i in range (num):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f'Введите координату {xy[i]}: '))
                coord.append(number)
                is_OK = True
            except ValueError:
                print('Ошибка ввода! Введите целое число!')
    return coord

def Distance(a, b):
    points_Distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return points_Distance


print("Введите координаты точки А: ")
pointA = Input_Number(2)
print("Введите координаты точки B: ")
pointB = Input_Number(2)

print(f"Длина отрезка АВ: {format(Distance(pointA, pointB), '.2f')}")
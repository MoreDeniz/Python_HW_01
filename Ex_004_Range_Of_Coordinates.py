# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input("Введите номер четверти: "))

if num == 1:
    print(f'Диапазон координат точки: x > 0 and y > 0')
if num == 2:
    print(f'Диапазон координат точки: x < 0 and y > 0')
if num == 3:
    print(f'Диапазон координат точки: x < 0 and y < 0')
if num == 4:
    print(f'Диапазон координат точки: x > 0 and y < 0')
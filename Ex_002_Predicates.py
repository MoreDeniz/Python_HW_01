# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def Input_Numbers(num):
    xyz = ["X", "Y", "Z"]
    my_list = []
    for i in range (num):
        my_list.append(input(f'Введите значение {xyz[i]}: '))
    return my_list

def Check_Predicate(num):
    left = not(num[0] or num[1] or num[2])
    right = not num[0] and not num[1] and not num[2]
    result = left == right
    return result

statement = Input_Numbers(3)
if Check_Predicate(statement) == True:
    print(f'Утверждение истинно')
else:
    print(f'Утверждение ложно')

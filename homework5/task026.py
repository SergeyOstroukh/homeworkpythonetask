
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# # *Пример:*
# # A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def stepen(num, step):
    if step <= 0:
        return 1
    else:
        return num * stepen(num, step-1)
print(stepen(3,5))


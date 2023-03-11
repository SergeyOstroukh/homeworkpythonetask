'''
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''
print('Введите трехзначное число: ')
number = int(input())
while number<99 or number >999:
    print('Введите трехзначное число: ')
    number = int(input())
    exit
if number > 99 and number  <1000:
    firstNumber = number%10
    twoNumber = number//10%10
    threeNumber = number//100
    symma= firstNumber+twoNumber+threeNumber
print(symma)
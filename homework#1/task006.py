'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
которая проверяет счастливость билета.
*Пример:*

385916 -> yes
123456 -> no
'''
print('Введите шестизначный номер билета: ')
numberTicket = input()
while len(numberTicket) != 6:
    print('Введите шестизначный номер билета: ')
    numberTicket= input()
    exit
if len(numberTicket) == 6:
    summa1 = int(numberTicket[0]) + int(numberTicket[1]) + int(numberTicket[2])
    summa2 = int(numberTicket[3]) + int(numberTicket[4]) + int(numberTicket[5])
if summa1 == summa2:
    print(f'Билет {numberTicket} счастливый!!!')
else: 
    print(f'Ваш билет {numberTicket} обычный :) ')
'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''
print('Введите общее количество сделанных журавликов кратное 6: ')
numbersCranes = int(input())
while numbersCranes%6 !=0:
    print('Введите общее количество сделанных журавликов коатное 6: ')
    numbersCranes = int(input())
    exit
if numbersCranes % 6 == 0:
    petyaNumberCranes= numbersCranes//6
    serejhaNumberCranes = petyaNumberCranes
    katyaNumberCranes = (petyaNumberCranes + serejhaNumberCranes)*2
    print(f'Всего изготовлено журавликов {numbersCranes}, Петя изготовил {petyaNumberCranes}, Катя изготовила {katyaNumberCranes}, Сережа изготовил {serejhaNumberCranes}')


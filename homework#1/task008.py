'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
'''

print('Введите количество долек по ширине: ')
widthChocolate = int(input())
print('Введите количество долек по длине: ')
lenghtChokolate = int(input())
print('Введите число долек которое хотим отломить от шоколадки: ')
numberOfPieces = int(input())
maxChokolatePiece = widthChocolate * lenghtChokolate
while numberOfPieces > maxChokolatePiece:
    print('Введено слишском большое значени, попробуйте еще раз: ')
    numberOfPieces = int(input())
    exit
while  maxChokolatePiece == numberOfPieces:
    print("Можно взять шоколадку целиком!!!")
    numberOfPieces = int(input())
    exit
if (maxChokolatePiece-numberOfPieces) % widthChocolate == 0 or (maxChokolatePiece-numberOfPieces) % lenghtChokolate == 0:
    print(f'Данное количество кусочков {numberOfPieces} можно отломить!!!')
else: 
    print(f'Невозможно отломить кусочек из {numberOfPieces} плиток!')


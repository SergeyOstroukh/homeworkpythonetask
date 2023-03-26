# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random

size_array1 = int(input('Введите размер массива #1: '))
array1 = []
for i in range(size_array1):
    array1.append(random.randint(1,10))

size_array2 = int(input('Введите размер массива №2 :'))
array2 = []
for j in range(size_array2):
    array2.append(random.randint(1,10))
newArr1 = set(array1)
newArr2 = set(array2)
resultArr = []
for num in newArr1:
    if num in array2:
        resultArr.append(num)
print(array1,array2)
print(f"повторяющиеся числа в массивах: ")
print(*resultArr)
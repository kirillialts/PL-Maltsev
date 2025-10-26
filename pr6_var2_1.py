array = []
x = int(input('введите количество элементов в массиве:'))
for i in range(x):
    num = int(input('введите число для массива:'))
    array.append(num)
array_min = min(array)
print(array_min)
array = [-3, -2, -1, 1, 2, 3]
array_plus = []
array_minus = []
for i in array:
    if i < 0:
        array_minus.append(i)
    else:
        array_plus.append(i)
print(f"массив с положительными значениями: {array_plus}")
print(f"массив с отрицательными значениями: {array_minus}")
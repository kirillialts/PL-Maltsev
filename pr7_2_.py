c = 0
list = []
for i in range(0, 3):
    a = int(input('введите длину прямоугольника:'))
    b = int(input('введите ширину прямоугольника:'))
    s = a * b
    list.append(s)
    c += 1
for x in range(0, 3):
    print(f'площадь {x+1} прямоугольника равна {list[x]} ')

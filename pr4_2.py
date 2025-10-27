a = int(input('введите первое число:'))
b = int(input('введите второе число:'))
if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
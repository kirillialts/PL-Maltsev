array = [-3, -2, -1, 1, 2, 3]
array_otr = []
array_pol = []
for i in array:
    if i < 0:
        array_otr.append(i)
    else:
        array_pol.append(i)
print(array_otr)
print(array_pol)
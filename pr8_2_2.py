A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('исходная матрица:')
for i in(A):
    print(i)
for x in range(len(A)):
    A[x][0], A[x][-1] = A[x][-1], A[x][0]
print('измененнная матрица:')
for i in(A):
    print(i)
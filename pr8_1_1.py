def magic_square(matrix):
    len_matrix = len(matrix)
    sum1 = sum(matrix[0])
    for i in range(len_matrix):
        sum2 = sum(matrix[i])
        if sum2 != sum1:
            return False
    for x in range(len_matrix):
        c = 0 
        for i in range(len_matrix):
            c += matrix[i][x]
        if c != sum1:
            return False
    return True

matrix = [
    [2, 7, 6],
    [9, 5, 1], 
    [4, 3, 8]
]

result = magic_square(matrix)
print(f'матрица является магическим квадратом: {result}')
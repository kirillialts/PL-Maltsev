def read_matrix_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
        return matrix

def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def is_magic_square(matrix):
    n = len(matrix)
    
    target_sum = sum(matrix[0])
    
    for i in range(n):
        if sum(matrix[i]) != target_sum:
            return False
    
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != target_sum:
            return False
    
    main_diag_sum = sum(matrix[i][i] for i in range(n))
    if main_diag_sum != target_sum:
        return False
    
    secondary_diag_sum = sum(matrix[i][n-1-i] for i in range(n))
    if secondary_diag_sum != target_sum:
        return False
    
    return True

def swap_first_and_last_columns(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][0], matrix[i][n-1] = matrix[i][n-1], matrix[i][0]
    return matrix

def create_test_files():
    magic_square = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
    
    regular_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    fio_group = "Мальцев Кирилл Романович УБ-52"
    
    with open(f"{fio_group}_vvod.txt", 'w', encoding='utf-8') as f:
        for row in magic_square:
            f.write(' '.join(map(str, row)) + '\n')

def main():
    fio_group = "Мальцев Кирилл Романович УБ-52"
    
    input_filename = f"{fio_group}_vvod.txt"
    output_filename = f"{fio_group}_vivod.txt"
    
    try:
        matrix = read_matrix_from_file(input_filename)
        
        output_text = ""
        
        output_text += "=== ЗАДАНИЕ 1 ===\n"
        output_text += "Исходная матрица:\n"
        for row in matrix:
            output_text += ' '.join(map(str, row)) + '\n'
        
        if is_magic_square(matrix):
            output_text += "\nМатрица ЯВЛЯЕТСЯ магическим квадратом\n"
        else:
            output_text += "\nМатрица НЕ ЯВЛЯЕТСЯ магическим квадратом\n"
        
        output_text += "\n=== ЗАДАНИЕ 2 ===\n"
        
        n = len(matrix)
        is_square = all(len(row) == n for row in matrix)
        
        if is_square:
            swapped_matrix = [row[:] for row in matrix]
            swapped_matrix = swap_first_and_last_columns(swapped_matrix)
            
            output_text += "Матрица после перестановки первого и последнего столбцов:\n"
            for row in swapped_matrix:
                output_text += ' '.join(map(str, row)) + '\n'
        else:
            output_text += "Матрица не является квадратной, задание 2 не выполнено.\n"
        
        write_to_file(output_filename, output_text)
        print(f"Результаты успешно записаны в файл: {output_filename}")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_filename} не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    create_test_files()
    main()

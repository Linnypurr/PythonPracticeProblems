def multiply_matrix(first_matrix, second_matrix):
    first_matrix_rows = len(first_matrix)
    first_matrix_columns = len(first_matrix[0])
    second_matrix_rows = len(second_matrix)
    second_matrix_columns = len(second_matrix[0])
    return_answer(first_matrix, second_matrix, first_matrix_rows, first_matrix_columns,
        second_matrix_rows, second_matrix_columns)

def return_answer(first_matrix, second_matrix, first_matrix_rows, first_matrix_columns,
    second_matrix_rows, second_matrix_columns):
    if not is_multipliable(first_matrix_columns, second_matrix_rows):
        print("Cannot multiple matrices")
    else:
        new_matrix = multiply(first_matrix, second_matrix, first_matrix_rows,
        first_matrix_columns, second_matrix_rows, second_matrix_columns)
        print_matrix(new_matrix)

def multiply(first_matrix, second_matrix, first_matrix_rows, first_matrix_columns,
    second_matrix_rows, second_matrix_columns):
    new_matrix = []
    for row_index in range(first_matrix_rows):
        new_row = []
        for column_index in range(second_matrix_columns):
            first_matrix_row = first_matrix[row_index]
            second_matrix_column = get_column(second_matrix, column_index)
            sum = multiply_add(first_matrix_row, second_matrix_column)
            new_row.append(sum)
        new_matrix.append(new_row)
    return new_matrix

def get_column(matrix, column_index):
    return [row[column_index] for row in matrix]

def multiply_add(row, column):
    length = len(row)
    sum = 0
    for index in range(length):
        sum += row[index] * column[index]
    return sum

def is_multipliable(first_matrix_columns, second_matrix_rows):
    return first_matrix_columns == second_matrix_rows

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == '__main__':
    first_matrix = [[1, 2],
                    [3, 4]]
    second_matrix = [[1, 3],
                     [2, 4]]

    multiply_matrix(first_matrix, second_matrix)

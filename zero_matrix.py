def process_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    has_zero_row_or_column(matrix, rows, columns)

def process_rows(matrix):
    has_zero_row = False
    for row in matrix:
        if row_is_all_zero(row):
            has_zero_row = True
    return has_zero_row

def process_columns(matrix, row_length, column_length):
    has_zero_column = False
    for column in range(column_length):
        column_array = []
        for row in range(row_length):
            column_array.append(matrix[row][column])
        if column_is_all_zero(column_array):
            has_zero_column = True
    return has_zero_column

def column_is_all_zero(column):
    return sum(column) == 0

def row_is_all_zero(row):
    return sum(row) == 0

def has_zero_row_or_column(matrix, rows, columns):
    is_column_with_zeros = process_columns(matrix, rows, columns)
    is_row_with_zeros = process_rows(matrix)
    is_both_with_zeros = is_column_with_zeros and is_row_with_zeros

    if is_both_with_zeros:
        print("This matrix contains row(s) and column(s) with all zeros")
    elif is_column_with_zeros:
        print("This matrix contains column(s) with all zeros")
    elif is_row_with_zeros:
        print("This matrix contains row(s) with all zeros")
    else:
        print("This matrix has no rows or columns with all zeros")

if __name__ == '__main__':
    matrix = [[0, 0, 0],
              [1, 0, 0],
              [4, 1, 0],
              [7, 0, 0]]

    process_matrix(matrix)

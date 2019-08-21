def process_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    return process_columns(matrix, rows, columns) or process_rows(matrix)

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

if __name__ == '__main__':
    matrix = [[0, 0, 8],
              [1, 0, 3],
              [4, 1, 6],
              [7, 0, 9]]
    print(process_matrix(matrix))

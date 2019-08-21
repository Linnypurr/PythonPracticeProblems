
def string_to_array(input_string):
    sudoku_array = [int(integer) for integer in input_string.split(",")]
    check_sudoku_board(sudoku_array)

def check_sudoku_board(sudoku_board):

    if check_sudoku_rows(sudoku_board) and check_sudoku_columns(sudoku_board):
        print(True)
    else:
        print(False)

def check_sudoku_rows(sudoku_board):
    is_valid_check = True
    for index_i in range(0, len(sudoku_board), 9):
        check_row_set = set([])
        for index_j in range(0, 9):
            check_row_set.add(sudoku_board[index_i + index_j])
        if not is_set_valid(check_row_set):
            is_valid_check = False
    return is_valid_check

def check_sudoku_columns(sudoku_board):
    is_valid_check = True
    for index_i in range(9):
        check_column_set = set([])
        for index_j in range(0, index_i + 73, 9):
            check_column_set.add(sudoku_board[index_i + index_j])
        if not is_set_valid(check_column_set):
            is_valid_check = False
    return is_valid_check

def is_set_valid(check_set):
    if len(check_set) != 9 or sum(check_set) != 45:
        return False
    return True


if __name__ == '__main__':
    input_string_2 = "1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9"
    input_string = "1, 2, 3, 4, 5, 6, 7, 9, 8, 4, 5, 6, 7, 8, 9, 1, 3, 2, 7, 8, 9, 1, 2, 3, 4, 6, 5, 5, 6, 7, 8, 9, 1, 2, 4, 3, 2, 3, 4, 5, 6, 7, 8, 1, 9, 8, 9, 1, 2, 3, 4, 5, 7, 6, 9, 1, 2, 3, 4, 5, 6, 8, 7, 6, 7, 8, 9, 1, 2, 3, 5, 4, 3, 4, 5, 6, 7, 8, 9, 2, 1"
    string_to_array(input_string)
n * (n-1) + 1

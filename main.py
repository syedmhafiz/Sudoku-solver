def find_nxt_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None            

def is_valid(puzzle, g, row, col):

    row_vals = puzzle[row]
    if g in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]    
    if g in col_vals:
        return False

    row_start = (row//3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == g:
                return False


def solve_sudoku(puzzle):

    row, col = find_nxt_empty(puzzle)


    if row is None:
        return True

    for g in range(1,10):
        if is_valid(puzzle, g, row, col):
            puzzle[row][col] = g

            if solve_sudoku(puzzle):
                return True


        puzzle[row][col] = -1


    return False    


if __name__ == '__main__':

    one_board = [[-1, -1, -1, -1, 1, 5, 9, -1, -1],
            [-1, 6, -1, 9, 2, 8, -1, -1, -1],
            [-1, -1, 4, 7, 6, -1, -1, 8, -1],
            [-1, -1, 8, 1, -1, -1, -1, 9, 6],
            [-1, 4, 7, -1, 9, -1, 2, -1, 8],
            [-1, -1, 1, -1, 8, -1, 7, -1, -1],
            [-1, -1, -1, -1, -1, -1, 5, 3, 1],
            [3, -1, -1, -1, -1, -1, -1, 2, -1],
            [-1, 5, -1, -1, -1, -1, -1, 4, -1]]

    print(solve_sudoku(one_board))
    print(one_board)        

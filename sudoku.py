# Author: Matthew Llanes
# Date: 12/1/2020
# Description: Playable Sudoku game, functions for solving the game

sudoku_game_instance = [[3, 0, 0, 1, 4, 0, 2, 0, 5],
                        [0, 0, 1, 0, 9, 8, 0, 0, 4],
                        [6, 0, 0, 2, 7, 0, 0, 0, 0],
                        [0, 9, 0, 0, 0, 0, 6, 0, 0],
                        [7, 2, 0, 6, 8, 9, 0, 5, 1],
                        [0, 0, 6, 0, 0, 0, 0, 2, 0],
                        [0, 0, 0, 0, 6, 4, 0, 0, 3],
                        [8, 0, 0, 3, 5, 0, 9, 0, 0],
                        [1, 0, 4, 0, 2, 7, 0, 0, 6]]

def valid_move(grid,x,y,num):
    """
    Checks whether or not given number is
    :param grid: current sudoku grid
    :param x: x-axis of number
    :param y: y-axis of number
    :param num: number to be tested if it's a possible spot
    :return: True if number is possible, false otherwise
    """
    # check if in-line spots contain num
    for i in range(0, 9):
        if grid[y][i] == num:   # across
            return False
        if grid[i][x] == num:   # up or down
            return False

    # check if 3*3 section contains num
    sec_x = (x // 3) * 3    # leftmost index of section
    sec_y = (y // 3) * 3    # topmost index of section
    for i in range(0, 3): # denotes y of section
        for j in range(0, 3):   # denotes x of section
            if grid[sec_y + i][sec_x + j] == num:   # check at each square within section
                return False

    return True # made it through every condition, this is indeed a valid move


def verify_solution(grid):
    """
    Verifies that a player's solution is valid in polynomial time
    :param grid: player given solution to a sudoku grid
    :return: True if valid solution, False otherwise
    """
    for y in range(0, 9):   # traverse lists
        for x in range(0, 9):   # traverse values in lists
            num = grid[y][x]
            if not valid_move(grid, x, y, num): # checks if move is valid
                return False
    return True # no invalid moves


def find_solution(grid):
    """
    Answers decision problem of whether a sudoku instance has a solution and provides said solution if so
    :param grid: unsolved sudoku grid
    :return: True if solution exists, false otherwise
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                for num in range(1, 10):
                    if valid_move(grid, x, y, num):
                        grid[y][x] = num
                        find_solution(grid)
                        if is_full(grid) == True:
                            return
                        grid[y][x] = 0
                return


def is_full(grid):
    """
    Checks if a sudoku grid is full
    :param grid: sudoku grid to check
    :return: True if full, False otherwise
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                return False
    return True


print(find_solution(sudoku_game_instance))
for i in range(0, 9):
    print(sudoku_game_instance[i])
print(verify_solution(sudoku_game_instance))
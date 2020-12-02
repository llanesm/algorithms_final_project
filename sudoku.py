# Author: Matthew Llanes
# Date: 12/1/2020
# Description: Playable Sudoku game, functions for solving the game

import math

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
    for i in range(0, len(grid)):
        if grid[y][i] == num and i != x:   # across
            return False
        if grid[i][x] == num and i != y:   # up or down
            return False

    # check if 3*3 section contains num
    sec_size = int(math.sqrt(len(grid)))
    sec_x = (x // sec_size) * sec_size    # leftmost index of section
    sec_y = (y // sec_size) * sec_size    # topmost index of section
    for i in range(0, sec_size): # denotes y of section
        for j in range(0, sec_size):   # denotes x of section
            if grid[sec_y + i][sec_x + j] == num and sec_y + i != y and sec_x + j != x:   # check at each square within section
                return False

    return True # made it through every condition, this is indeed a valid move


def verify_solution(grid):
    """
    Verifies that a player's solution is valid in polynomial time
    :param grid: player given solution to a sudoku grid
    :return: True if valid solution, False otherwise
    """
    for y in range(0, len(grid)):   # traverse lists
        for x in range(0, len(grid)):   # traverse values in lists
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
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):
            if grid[y][x] == 0:	# is empty
                for num in range(1, 10):	# usable numbers
                    if valid_move(grid, x, y, num):	# if valid move is true
                        grid[y][x] = num	# insert number into square
                        find_solution(grid)	# recursive call to find next insert
                        if is_full(grid) == True:	# grid is full, we're done'
                            return True
                        grid[y][x] = 0	# backtrack when a value no longer works, makes space empty
                return False	# no solution


def is_full(grid):
    """
    Checks if a sudoku grid is full
    :param grid: sudoku grid to check
    :return: True if full, False otherwise
    """
    for y in range(0, len(grid)):
        for x in range(0, len(grid)):
            if grid[y][x] == 0:
                return False
    return True


def main():
	find_solution(sudoku_game_instance)
	for i in range(0, len(sudoku_game_instance)):
		print(sudoku_game_instance[i])
	print(verify_solution(sudoku_game_instance))
	
	
if __name__ == '__main__':
	main()

# Author: Matthew Llanes
# Date: 12/1/2020
# Description: Playable Sudoku game, functions for solving the game, verifying a solution

import math
import random


class SudokuGame:
    """Represents sudoku game instance"""

    def __init__(self, n=3):
        """initializes game board"""
        self.grid = []
        self.make_grid(n)

    def make_grid(self, n):
        """Generates sudoku puzzle of given section size n"""
        # create empty grid
        for column in range(0, n ** 2):
            row = []
            for i in range(0, n ** 2):
                row.append(0)
            self.grid.append(row)

        # populate one diagonal set of sections
        for i in range(0, n):
            start = i * n
            end = start + n
            for y in range(start, end):
                for x in range(start, end):
                    num = random.randint(1, n ** 2)
                    while not self.valid_move(x, y, num):   # if the first number doesn't work, find one that does
                        num = random.randint(1, n ** 2)
                    self.grid[y][x] = num   # insert it into the grid

        self.find_solution()    # populate the rest of the grid

        # remove a number of random integers from the grid
        # TODO find an appropriate amount k of zeroes to take out so it works with all sizes n
        count = int((n ** 4) * 0.55)   # ratio of easy sudoku game I originally based program off of
        while count != 0:
            x = random.randint(0, (n ** 2) - 1)
            y = random.randint(0, (n ** 2) - 1)
            if self.grid[y][x] != 0:
                self.grid[y][x] = 0
                count -= 1
            else:
                continue

    def valid_move(self, x, y, num):
        """
        Checks whether or not given number is valid in given location
        :param x: x-axis of number
        :param y: y-axis of number
        :param num: number to be tested if it's a possible spot
        :return: True if number is possible, false otherwise
        """
        # make sure num is within range
        if num < 1 or num > len(self.grid):
            return False

        # check if in-line spots contain num
        for i in range(0, len(self.grid)):
            if self.grid[y][i] == num and i != x:   # across
                return False
            if self.grid[i][x] == num and i != y:   # up or down
                return False

        # check if 3*3 section contains num
        sec_size = int(math.sqrt(len(self.grid)))
        sec_x = (x // sec_size) * sec_size    # leftmost index of section
        sec_y = (y // sec_size) * sec_size    # topmost index of section
        for i in range(0, sec_size): # denotes y of section
            for j in range(0, sec_size):   # denotes x of section
                # check at each square within section
                if self.grid[sec_y + i][sec_x + j] == num and sec_y + i != y and sec_x + j != x:
                    return False

        return True     # made it through every condition, this is indeed a valid move

    def verify_solution(self):
        """
        Verifies that a player's solution is valid in polynomial time
        :return: True if valid solution, False otherwise
        """
        for y in range(0, len(self.grid)):   # traverse lists
            for x in range(0, len(self.grid)):   # traverse values in lists
                num = self.grid[y][x]
                if not self.valid_move(x, y, num): # checks if move is valid
                    return False
        return True     # no invalid moves

    def find_solution(self):
        """
        Answers decision problem of whether a sudoku instance has a solution and provides said solution if so
        :return: True if solution exists, false otherwise
        """
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid)):
                if self.grid[y][x] == 0:    # is empty
                    for num in range(1, len(self.grid) + 1):    # usable numbers
                        if self.valid_move(x, y, num):  # if valid move is true
                            self.grid[y][x] = num   # insert number into square
                            self.find_solution()    # recursive call to find next insert
                            if self.is_full():  # grid is full, we're done'
                                return True
                            self.grid[y][x] = 0	# backtrack when a value no longer works, makes space empty
                    return False    # no solution

    def is_full(self):
        """
        Checks if a sudoku grid is full
        :return: True if full, False otherwise
        """
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid)):
                if self.grid[y][x] == 0:
                    return False
        return True

    def print_grid(self):
        """Prints sudoku grid to console"""
        for i in range(0, len(self.grid)):
            print(self.grid[i])

    def make_move(self, x, y, num):
        """Inserts player move onto grid, ensuring it is a valid move before doing so"""
        if self.valid_move(x, y, num):
            self.grid[y][x] = num



def main():
    """Allows user to play the sudoku game or have a solution auto generated in the console"""
    game = SudokuGame(3)
    game.print_grid()
    choice = input("Would you like to play the board or would you like a "
                   "solution to be generated for you? Enter 'Play' or 'Generate' ")
    choice.lower()
    if choice == "play":
        while not game.is_full():
            x = int(input("What x-coordinate to place your number? "))
            y = int(input("What y-coordinate to place your number? "))
            num = int(input("What number would you like to place?"))
            game.make_move(x, y, num)
            game.print_grid()
        if not game.verify_solution():
            print("WRONG SOLUTION")
        else:
            print("YOU WIN")
    else:
        game.find_solution()
        game.print_grid()


if __name__ == '__main__':
    main()

# Sudoku.py is a sudoku generator that uses a recursive backtracking
# algorithm to check if a given puzzle only has one solution. It can also
# create its own puzzle
# Sources: https://www.101computing.net/sudoku-generator-algorithm/
# 5/6/22
# author = Charlotte Miller

import pygame
from random import randint, shuffle
from time import sleep

# main grid of puzzle, using separate lines of code for each line so that
# puzzle can be easily changed square by square
grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

colcens = [233, 299.5, 366.5, 433, 499.5, 566.5, 633, 699.5, 766.5]
rowcens = [133, 199.5, 266.5, 333, 399.5, 466.5, 533, 599.5, 666.5]

pygame.init()
pygame.font.init()
favFont = pygame.font.Font('freesansbold.ttf', 30)
background_color = (234, 212, 252)
black = (0, 0, 0)
green = (0, 255, 0)

def gameSetup():
    global screen, running
    screen = pygame.display.set_mode(size=(1000, 800))
    screen.fill(background_color)
    pygame.display.set_caption("Sudoku")
    running = True
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # to put in a puzzle and have it be solved, uncomment gridCreate
                # and solveGrid and put the puzzle into the grid (lines 15-23)
                # to have a puzzle be created, uncomment genSolved and genPuzzle
                genSolved(grid)
                genPuzzle(grid)
                # gridCreate(grid)
                # solveGrid(grid)

def textPrinting(text, cx, cy, colour):
    global favFont
    # pygame.draw.rect(screen, background_color, (cx - 20, cy - 20, cx + 20, cy + 20))
    thing = favFont.render(text, True, colour)
    textRect = thing.get_rect()
    textRect.center = (cx, cy)
    if text == "0":
        pygame.draw.rect(screen, background_color, textRect)
        pass
    else:
        pygame.draw.rect(screen, background_color, textRect)
        screen.blit(thing, textRect)


# used to draw simple lines of grid
def drawLine(ix, iy, iix, iiy, size):
    pygame.draw.line(screen, black, [ix,iy], [iix, iiy], size)


# draw initial board
def gridCreate(grid):
    # outer lines
    drawLine(200, 100, 800, 100, 5)
    drawLine(800, 100, 800, 700, 5)
    drawLine(800, 700, 200, 700, 5)
    drawLine(200, 700, 200, 100, 5)
    # big inner 3x3
    drawLine(400, 100, 400, 700, 4)
    drawLine(600, 100, 600, 700, 4)
    drawLine(200, 300, 800, 300, 4)
    drawLine(200, 500, 800, 500, 4)
    # vertical inner lines
    drawLine(266, 100, 266, 700, 2)
    drawLine(333, 100, 333, 700, 2)
    drawLine(466, 100, 466, 700, 2)
    drawLine(533, 100, 533, 700, 2)
    drawLine(666, 100, 666, 700, 2)
    drawLine(733, 100, 733, 700, 2)
    # horizontal inner lines
    drawLine(200, 166, 800, 166, 2)
    drawLine(200, 233, 800, 233, 2)
    drawLine(200, 366, 800, 366, 2)
    drawLine(200, 433, 800, 433, 2)
    drawLine(200, 566, 800, 566, 2)
    drawLine(200, 633, 800, 633, 2)
    # prints each number to its box, making sure to not actually print any 0's
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                pass
            else:
                textPrinting(str(grid[row][col]), colcens[col], rowcens[row], black)
    pygame.display.flip()

# checks if puzzle is solved/complete
def isComplete(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return False
    return True

# solves given puzzle
def solveGrid(grid):
    # Find next empty cell
    global counter
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            for value in range(1, 10):
                # Check that  value has not already been used on this row
                if not (value in grid[row]):
                    # Check that  value has not already been used on this column
                    if not value in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                        # Identify which square we're in
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        # Check that value has not already been used on this 3x3
                        if not value in (square[0] + square[1] + square[2]):
                            # textPrinting(str(value), colcens[col], rowcens[row], black)
                            grid[row][col] = value
                            pygame.display.flip()
                            if isComplete(grid):
                                counter += 1
                                break
                            else:
                                if solveGrid(grid):
                                    return True
            break
    grid[row][col] = 0

possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# randomly creates a valid solution
def solutionCreation(grid):
    # Find next empty cell
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            shuffle(possible_nums)
            for value in possible_nums:
                # Check that value has not already been used on this row
                if not (value in grid[row]):
                    # Check that value has not already been used on this column
                    if not value in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                        # Identify which square we're in
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        # Check that value has not already been used in this 3x3
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if isComplete(grid):
                                return True
                            else:
                                if solutionCreation(grid):
                                    return True
            break
    grid[row][col] = 0


# takes the 100% solved puzzle and makes it something in need of solving with
# only one solution
def genPuzzle(grid):
    global counter
    # increase number of attempts to make puzzle harder
    attempts = 5
    counter = 1
    while attempts > 0:
        print(attempts)
        # select random cell that isn't empty yet
        row = randint(0, 8)
        col = randint(0, 8)
        while grid[row][col] == 0:
            row = randint(0, 8)
            col = randint(0, 8)
        # remember current value in case it cannot be removed without creating
        # more than 1 solution
        backup = grid[row][col]
        grid[row][col] = 0
        textPrinting("0", colcens[col], rowcens[row], black)
        # create a copy of grid so we can mess with it safely
        copyGrid = []
        for r in range(0, 9):
            copyGrid.append([])
            for c in range(0, 9):
                copyGrid[r].append(grid[r][c])

        # Count number of solutions grid has
        counter = 0
        solveGrid(copyGrid)
        # if number of solutions isn't 1 we need to restore the original
        if counter != 1:
            grid[row][col] = backup
            textPrinting(str(backup), colcens[col], rowcens[row], black)
            print(row, col, backup)
            # allows program to try something new, more attempts means it won't
            # stop removing numbers as quickly
            attempts -= 1
    print("Puzzle ready for attempting!")

# generates a 100% solved puzzle
def genSolved(grid):
    solutionCreation(grid)
    gridCreate(grid)

if __name__ == '__main__':
    gameSetup()
    '''
    if solveGrid(grid):
        print("Grid has been solved")
    else:
        print("Grid has not been solved")
    '''
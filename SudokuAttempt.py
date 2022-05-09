# Sudoku.py is
# 5/6/22
# author = Charlotte Miller

import pygame
from random import randint
from time import sleep

# main grid of puzzle, using separate lines of code for each line so that
# puzzle can be easily changed square by square
grid = []
grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])

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
                gridCreate(grid)
                solveGrid(grid)

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

# solves puzzle
def solveGrid(grid):
    problem = False
    for row in range(9):
        for col in range(9):
            if problem:
                print()
                if col == 0:
                    row -= 1
                    col = 7
                elif col == 1:
                    row -= 1
                    col = 8
                else:
                    col -= 2
            print(row, col)
            if grid[row][col] == 0:
                for i in range(1, 10):
                    if problem:
                        i = grid[row][col] + 1
                        grid[row][col] = 0
                        textPrinting("0", colcens[col - 1], rowcens[row], black)
                    problem = False
                    if i not in (grid[row]):
                        if i not in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                            # which 3x3 are we working on of the 9
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [grid[j][0:3] for j in range(0, 3)]
                                elif col < 6:
                                    square = [grid[j][3:6] for j in range(0, 3)]
                                else:
                                    square = [grid[j][6:9] for j in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[j][0:3] for j in range(3, 6)]
                                elif col < 6:
                                    square = [grid[j][3:6] for j in range(3, 6)]
                                else:
                                    square = [grid[j][6:9] for j in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[j][0:3] for j in range(6, 9)]
                                elif col < 6:
                                    square = [grid[j][3:6] for j in range(6, 9)]
                                else:
                                    square = [grid[j][6:9] for j in range(6, 9)]
                            if i not in square[0] and i not in square[1] and i not in square[2]:
                                textPrinting(str(i), colcens[col], rowcens[row], black)
                                grid[row][col] = i
                                print(i, row, col)
                                pygame.display.flip()
                                if isComplete(grid):
                                    textPrinting("Grid complete!")
                                    return True
                                break
                if grid[row][col] == 0:
                    print("Backtrack int")
                    problem = True
                else:
                    continue
    # need to figure out how to tell program you messed up, go back to your
    # last successful guess and increment it up 1 (ie. 9 failed in (1, 8) so
    # go back to that 6 you put in (1, 7) and see if making it a 7 helps)
    print("Backtrack ext")
    grid[row][col] = 0
    solveGrid(grid)


if __name__ == '__main__':
    gameSetup()
    if solveGrid(grid):
        print("Grid has been solved")
    else:
        print("Grid has not been solved)")
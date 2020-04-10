""" This game was Conway's Game of Life, I would definetly recommend reading about it. Especially, if you love
maths http://www.math.com/students/wonders/life/life.html, describes the concept really well. Some patterns can go on
forever, like the glider."""

import random, time, copy
width = 10
height = 10

nextCells = []
for x in range(width):
    column = []
    for y in range(height):
        column.append(random.choice(["#", " "]))
    nextCells.append(column)
while True:
    print("\n\n\n\n\n")
    currentCells = copy.deepcopy(nextCells)
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end=" ")
        print()

    for x in range(width):
        for y in range(height):
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors +=1
            if currentCells[x][aboveCoord] == "#":
                numNeighbors +=1
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors +=1
            if currentCells[leftCoord][y] == "#":
                numNeighbors +=1
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors +=1
            if currentCells[x][belowCoord] == "#":
                numNeighbors +=1
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors +=1
            if currentCells[rightCoord][y] == "#":
                numNeighbors +=1

            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                currentCells[x][y] = "#"
            else:
                nextCells[x][y] = " "
    time.sleep(2)


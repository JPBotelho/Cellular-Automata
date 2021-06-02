import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
from random import randrange, randint, uniform
import sys
import math
import time

import numpy as np

from matplotlib import pylab as plt
np.set_printoptions(threshold=sys.maxsize)

iterations = 10
def evaluateNeighbours(xc, yc):
    #bottom left index
    blX = xc-1
    blY = yc-1

    validNeighbours = 0
    activeNeighbours = 0
    for x in range(0, 3):
        for y in range(0, 3):
            sX = blX +x;
            sY = blY +y
            #ignore current point
            if(x == 0 and y == 0):
                continue
            if(sY < 0 or sX < 0):
                continue
            if(sX >= imageWidth or sY >= imageHeight):
                continue
            
            val = grid[sX][sY][0]
            if(val == 255):
                validNeighbours+=1;
            activeNeighbours+=1;

            
    if validNeighbours / activeNeighbours > 0.5:
        return 1
    if validNeighbours / activeNeighbours < 0.5:
        return -1
    else:
        return 0


borderWidth = 3
imageWidth = 512
imageHeight = 512
grid = []
for x in range(0, imageWidth):
    cell = []
    for y in range(0, imageHeight):
        currentColor = 0
        #Left Border
        if(x < borderWidth):
            currentColor = 0
        elif(x > imageWidth - borderWidth-1):
            currentColor = 0
        elif(y < borderWidth):
            currentColor = 0
        elif(y > imageHeight - borderWidth-1):
            currentColor = 0
        else:
            randomCol = randrange(0, 100)
            if(randomCol > 50):
                currentColor = 255
        cell.append([currentColor,currentColor,currentColor])
    grid.append(cell)


for iter in range(0, iterations):
    for x in range(0, imageWidth):
        for y in range(0, imageHeight):
            result = evaluateNeighbours(x, y)
            if(result == 1):
                grid[x][y] = [255, 255, 255]
            elif result == -1:
                grid[x][y] = [0, 0, 0]


img = Image.new("RGB", (imageWidth, imageHeight), "black")
pixels = img.load()
for x in range(0, imageWidth):
    for y in range(0, imageHeight):
        pixels[x, y] = (grid[x][y][0], grid[x][y][1], grid[x][y][2])

img.show();
img.save("testCell.png")


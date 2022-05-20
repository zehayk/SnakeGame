# SNAKE SnakeGame #
import datetime
import random
import sys
import time
from tkinter import Tk, Canvas, mainloop, PhotoImage
import keyboard

mapSizeX = 15
mapSizeY = 15
sizePixel = 25



board = [[]]

width = mapSizeX * sizePixel
height = mapSizeY * sizePixel
window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#008000")
canvas.pack()


class Snake:
    def __init__(self):
        self.direction = "up"
        self.previousDirection = "up"
        self.lastMoved = datetime.datetime.now()
        self.coords = []
        for i in range(5):
            self.coords.append(f"{round(mapSizeX / 2)},{round(mapSizeY / 2) + i}")


    def move(self):
        if keyboard.is_pressed("w"):
            if self.previousDirection != "down":
                self.direction = "up"
        elif keyboard.is_pressed("a"):
            if self.previousDirection != "right":
                self.direction = "left"
        elif keyboard.is_pressed("d"):
            if self.previousDirection != "left":
                self.direction = "right"
        elif keyboard.is_pressed("s"):
            if self.previousDirection != "up":
                self.direction = "down"

        if (datetime.datetime.now() - self.lastMoved).total_seconds() < 0.3:
            return
        else:
            self.lastMoved = datetime.datetime.now()
            self.previousDirection = self.direction

        direction = self.direction

        modX = 0
        modY = 0

        if direction == "up":
            modY -= 1
        elif direction == "down":
            modY += 1
        elif direction == "left":
            modX -= 1
        elif direction == "right":
            modX += 1

        head = self.coords[0].split(",")
        newX = int(head[0]) + modX
        newY = int(head[1]) + modY
        newCoord = f"{newX},{newY}"
        # check if lose
        if mapSizeX < newX or newX < 0 or mapSizeY < newY or newY < 0:
            print("you lose")
            sys.exit(0)
        for coord in self.coords:
            if newCoord == coord:
                print("you lose")
                sys.exit(0)

        # check if apple
        if newCoord != myGame.apple:
            self.draw(self.coords[-1])
            self.coords.pop(-1)
        else:
            myGame.makeNewApple()


        self.coords.insert(0, newCoord)
        self.draw()

    def draw(self, coord=None):
        if coord is None:
            for i in range(len(self.coords)):
                x = int(self.coords[i].split(",")[0]) * sizePixel
                y = int(self.coords[i].split(",")[1]) * sizePixel
                canvas.create_rectangle(x, y, x + sizePixel, y + sizePixel, fill='blue', outline='black')
        else:
            x = int(coord.split(",")[0]) * sizePixel
            y = int(coord.split(",")[1]) * sizePixel
            canvas.create_rectangle(x, y, x + sizePixel, y + sizePixel, fill='green', outline='black')


class SnakeGame:
    def __init__(self):
        self.drawBoard()
        self.makeNewApple()
        self.snake = Snake()

    def makeNewApple(self):
        coordsStr = ""
        for coord in self.snake.coords:
            coordsStr += coord + " "

        while True:
            appleX = random.randrange(mapSizeX)
            appleY = random.randrange(mapSizeY)

            self.apple = f"{appleX},{appleY}"
            if self.apple not in coordsStr:
                break

        x = appleX * sizePixel
        y = appleY * sizePixel
        canvas.create_rectangle(x, y, x + sizePixel, y + sizePixel, fill='red', outline='red')

    def drawBoard(self):
        for i in range(mapSizeX):
            for k in range(mapSizeY):
                x = i * sizePixel
                y = k * sizePixel
                canvas.create_rectangle(x, y, x + sizePixel, y + sizePixel, fill='green', outline='black')


def runGame():
    myGame.snake.move()
    window.after(50, runGame)


myGame = SnakeGame()
runGame()
window.mainloop()


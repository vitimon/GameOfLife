
from LifeGame import *
from tkinter import *


gameLines = 30
gameColumns = 30
boardHeight = 600
boardWidth = 600
boardBackground = "white"
cellColor = "black"
cellHeight = boardHeight/gameLines
cellWidth = boardWidth/gameColumns
frameTime = 300

root = Tk()
root.title("Game Of Life")
root.geometry('800x640')


class Board(Canvas):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.boardState = LifeGame(gameLines,gameColumns,initializer="RANDOM")
        self.printState()
        self.updateState()

    def printState(self):
        self.delete("all")
        for line in range(self.boardState.lines):
            for column in range(self.boardState.columns):
                if self.boardState.matrix[line][column] > 0:
                    x0,y0,x1,y1 = column*cellWidth, line*cellHeight, (column + 1)*cellWidth, (line + 1)*cellHeight
                    self.create_rectangle(x0,y0,x1,y1,fill=cellColor)
    
    def updateState(self):
        self.boardState = self.boardState.nextState()
        self.printState()
        self.after(frameTime,self.updateState)





canvas = Board(root, height = boardHeight, width = boardWidth,bg = boardBackground)

canvas.pack()


root.mainloop()

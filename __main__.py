from LifeGame import *
from tkinter import *

gameLines = 10
gameColumns = 10
boardHeight = 600
boardWidth = 600
boardBackground = "white"
cellColor = "black"
cellHeight = boardHeight/gameLines
cellWidth = boardWidth/gameColumns
frameTime = 500

root = Tk()
root.title("Game Of Life")
root.geometry('800x640')

class Board(Canvas):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.boardState = LifeGame(gameLines,gameColumns,initializer="RANDOM")
        self.printState()
        self.running = 0

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
        if self.running: self.after(frameTime,self.updateState)

    def resetBoard(self,event):
        self.boardState = LifeGame(gameLines,gameColumns,initializer="RANDOM")
        self.printState()
        if self.running: self.updateState()

    def killBoard(self,event):
        self.boardState = LifeGame(gameLines,gameColumns,initializer="EMPTY")
        self.printState()
        if self.running: self.updateState()

    def stoprun(self,event):
        self.running = self.running ^ 1
        if self.running: self.updateState()
        
commandBar = Frame(root)
toggleButton = Button(commandBar,text = "RUN - STOP")
resetButton = Button(commandBar, text = "RESET")
killButton = Button(commandBar, text = "KILL")
canvas = Board(root, height = boardHeight, width = boardWidth,bg = boardBackground)

toggleButton.pack()
toggleButton.bind('<Button-1>', canvas.stoprun)
resetButton.pack()
resetButton.bind('<Button-1>', canvas.resetBoard)
killButton.pack()
killButton.bind('<Button-1>', canvas.killBoard)
commandBar.grid()
canvas.grid(column = 3, row = 0)

root.mainloop()

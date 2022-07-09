from Matrix import Matrix
from time import sleep
from os import system

clear = lambda: system('clear')

def makeRandomPattern(lines,columns):
    randomPattern = []
    for element in range(2*lines + 2*columns + 4):
        randomPattern += [randint(0,1)]
    return randomPattern

def simulateRandom(size,timer=.5):
    initialState = LifeGame(size,size,initializer="RANDOM")
    return initialState.simulateCGoL(100,timer)

class LifeGame(Matrix):
    def __str__(self):
        stringfyed = ""
        for line in self.matrix:
            for column in line:
                if column == 0: stringfyed += " "
                if column == 1: stringfyed += "\u25A0"
            stringfyed += "\n"
        return stringfyed
    
    def __filterCell(self,x,y,pattern = [0]):
        size = len(pattern)
        if y < -1:
            raise("Y OUT OF LESSER BOUNDARIES")
        if y > self.lines:
            raise("Y OUT OF UPPER BOUNDARIES")
        if x < -1:
            raise("X OUT OF LEFTMOST BOUNDARIES")
        if x > self.columns:
            raise("X OUT OF RIGHTMOST BOUNDARIES")
        if y == -1:
            return pattern[(x+1)%size]
        if x == self.columns:
            return pattern[(self.columns + y + 2 )%size]
        if y == self.lines:
            return pattern[(2*self.columns + self.lines -x + 2)%size ]
        if x == -1:
            return pattern[(2*self.columns + 2*self.lines - y + 3)%size]
        return 1 if self.matrix[y][x] > 0 else 0

    def __cellquence(self,x,y,externalPattern =[0]):
        currentState = self.matrix[y][x]
        nextState = 0
        lives = False
        for delta1 in range(-1,2):
            for delta2 in range(-1,2):
                nextState += self.__filterCell(x+delta1,y+delta2, externalPattern)
        if (nextState == 3) | (nextState - currentState) == 3: lives = True
        #print("cell: {},{} ---- sum: {}, current: {}  so it lives? {}".format(x,y,nextState,currentState,lives))
        return 1 if (nextState == 3) | (nextState - currentState) == 3 else 0

    def nextState(self,borderPattern =[0]):
        nextMatrix = []
        for line in range(self.lines):
            nextMatrix+= [[]]
            for column in range(self.columns):
                nextMatrix[line] += [ self.__cellquence(column,line,borderPattern) ]
        return LifeGame(self.lines,self.columns,nextMatrix)
    
    def simulateCGoL(self,steps = 1,timer = 1,pattern = [0]):
        print(self)
        pastStep = self
        simulated = self.nextState(pattern)
        while(steps > 0):
            if (simulated.matrix == pastStep.matrix): return "STABILIZED before {} steps completion in the shape:\n{}".format(steps,simulated)
            if (simulated.matrix == simulated.lines*[simulated.columns*[0]]): return "DIED before {} steps completion".format(steps)
            print(steps)
            print(simulated)
            pastStep = simulated
            simulated = simulated.nextState(pattern)
            steps -= 1
            sleep(timer)
            clear()
        return "final matrix:\n{}".format(simulated)

    def insertBlock(self,x,y):
        if (x > self.columns - 2): raise("OUT OF BOUNDS")
        if (y > self.lines - 2): raise("OUT OF BOUNDS")
        if (x < 0): raise("OUT OF BOUNDS")
        if (x < 0): raise("OUT OF BOUNDS")
        self.matrix[y][x] = 1
        self.matrix[y + 1][x] = 1
        self.matrix[y][x + 1] = 1
        self.matrix[y + 1][x + 1] = 1
        return self

class BorderlessLifeGame(LifeGame):
    def __filterCell(self,x,y):
        if y < -1:
            raise("Y OUT OF LESSER BOUNDARIES")
        if y > self.lines:
            raise("Y OUT OF UPPER BOUNDARIES")
        if x < -1:
            raise("X OUT OF LEFTMOST BOUNDARIES")
        if x > self.columns:
            raise("X OUT OF RIGHTMOST BOUNDARIES")
        if y == -1:
            if x == -1: return self.matrix[-1][-1]
            if x == self.columns: return self.matrix[-1][0]
            return self.matrix[-1][x]
        if x == self.columns:
            if y == self.lines: return self.matrix[0][0]
            return self.matrix[y][0]
        if y == self.lines: 
            if x == -1: return self.matrix[0][-1]
            return self.matrix[0][x]
        if x == -1:
            return self.matrix[y][-1]
        return self.matrix[y][x]

    def __cellquence(self,x,y):
        currentState = self.matrix[y][x]
        nextState = 0
        for delta1 in range(-1,2):
            for delta2 in range(-1,2):
                nextState += self.__filterCell(x+delta1,y+delta2)
        #print("cell: {},{} ---- sum: {}, current: {}  so it lives? {}".format(x,y,nextState,currentState,lives))
        return 1 if (nextState == 3) | (nextState - currentState) == 3 else 0

    def nextState(self):
        nextMatrix = []
        for line in range(self.lines):
            nextMatrix+= [[]]
            for column in range(self.columns):
                nextMatrix[line] += [ self.__cellquence(column,line) ]
        return BorderlessLifeGame(self.lines,self.columns,nextMatrix)
    
    
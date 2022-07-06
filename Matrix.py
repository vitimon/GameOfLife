
from random import randint


class Matrix:
    matrix = []
    lines = 0
    columns = 0

    def makeEmptyMatrix(self,lines,columns):
        return Matrix(lines,columns,[[0]*columns]*lines)

    def makeFullMatrix(self,lines,columns):
        return Matrix(lines,columns,[[1]*columns]*lines)
    
    def makeRandomBinaryMatrix(self,lines,columns):
        binaryMatrix = []
        for line in range(lines):
            binaryMatrix += [[]]
            for column in range(columns):
                binaryMatrix[line] += [randint(0,1)]
        return Matrix(lines,columns,binaryMatrix)

    def __init__(self, n=0, m=0, v=[[]], initializer = ""):
        self.lines = n
        self.columns = m
        if initializer == "EMPTY": 
            self.matrix = self.makeEmptyMatrix(n,m).matrix
        elif initializer == "FULL":
            self.matrix = self.makeFullMatrix(n,m).matrix
        elif initializer == "RANDOM": 
            self.matrix = self.makeRandomBinaryMatrix(n,m).matrix
        else:
            self.matrix = []
            for line in range(self.lines):
                self.matrix += [[]]
                for column in range(self.columns):
                    self.matrix[line] += [v[line][column]]


    def __add__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be added.")
        if (self.lines != other.lines) | (self.columns != other.columns):
            raise("Matrixes must have the same number of lines and columns.")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(self.columns):
                result[line] += [self.matrix[line][column] + other.matrix[line][column]]
        return Matrix(self.lines,self.columns, result)

    def __sub__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be subtracted.")
        if (self.lines != other.lines) | (self.columns != other.columns):
            raise("Matrixes must have the same number of lines and columns.")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(self.columns):
                result[line] += [self.matrix[line][column] - other.matrix[line][column]]
        return Matrix(self.lines,self.columns, result)


    def __mul__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be multiplied.")
        if (self.lines != other.columns) | (self.columns != other.lines):
            raise("Matrixes must be multiplicable: (LinesA = ColumnsB) & (ColumnsA = LinesB).")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(other.columns):
                element = 0
                for stack in range(self.columns):
                    element += self.matrix[line][stack]*other.matrix[stack][column]
                result[line] += [element]
        return Matrix(self.lines,other.columns, result)

    def __or__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be 'ored'.")
        if (self.lines != other.lines) | (self.columns != other.columns):
            raise("Matrixes must have the same number of lines and columns.")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(self.columns):
                result[line] += [self.matrix[line][column] | other.matrix[line][column]]
        return Matrix(self.lines,self.columns, result)
    
    def __xor__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be 'xored'.")
        if (self.lines != other.lines) | (self.columns != other.columns):
            raise("Matrixes must have the same number of lines and columns.")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(self.columns):
                result[line] += [self.matrix[line][column] ^ other.matrix[line][column]]
        return Matrix(self.lines,self.columns, result)

    def __str__(self):
        stringfyed = ""
        for line in self.matrix:
            stringfyed += str(line) + "\n"
        return stringfyed
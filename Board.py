from Node import *
from Constants import *

class Board:
    def __init__(self):
        self.playing = "b"
        self.matrix = [[Node(x, y) for x in range(SIZE)] for y in range(SIZE)]
    
    def changePlayer(self):
        if self.playing == "b":
            self.playing = "w"
        else:
            self.playing = "b"
    
    def show(self):
        for x in range(SIZE):
            for y in range(SIZE):
                self.matrix[y][x].show()
    
    def inBounds(self, x, y):
        return x>MARGIN and x<XMAX and y>MARGIN and y<YMAX
    
    def getNodes(self, x, y):
        return ((x - MARGIN) // CELLDIM, (y - MARGIN) // CELLDIM)
    
    def checkHover(self, x, y):
        if self.inBounds(x, y):
            xNode, yNode = self.getNodes(x, y)
            self.matrix[yNode][xNode].showTransparent(self.playing)
    
    def checkCapture(self, x, y):
        pass
    
    def checkClick(self, x, y):
        if self.inBounds(x, y):
            xNode, yNode = self.getNodes(x, y)
            node = self.matrix[yNode][xNode]
            if node.isEmpty():
                if self.playing == "b":
                    node.setBlack()
                elif self.playing == "w":
                    node.setWhite()
                self.checkCapture(xNode, yNode)
                self.changePlayer()
    
    
    
    
    
    
    
    
    
    
    
    
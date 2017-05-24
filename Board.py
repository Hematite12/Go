from Node import *
from Constants import *

from collections import deque

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
    
    def inPosBounds(self, x, y):
        return x>MARGIN and x<XMAX and y>MARGIN and y<YMAX
    
    def inBoardBounds(self, x, y):
        return x>-1 and x<SIZE and y>-1 and y<SIZE
    
    def getNodes(self, x, y):
        return ((x - MARGIN) // CELLDIM, (y - MARGIN) // CELLDIM)
    
    def checkHover(self, x, y):
        if self.inPosBounds(x, y):
            xNode, yNode = self.getNodes(x, y)
            self.matrix[yNode][xNode].showTransparent(self.playing)
    
    def evalLiberties(self, x, y, player):
        if self.inBoardBounds(x, y):
            node = self.matrix[y][x]
            queue = deque([node])
            searched = []
            while len(queue) > 0:
                node = queue.pop()
                if not node.searched:
                    if node.isEmpty():
                        for capNode in searched:
                            capNode.searched = False
                        return
                    if node.piece != player:
                        node.searched = True
                        searched.append(node)
                        if self.inBoardBounds(node.x, node.y+1):
                            queue.appendleft(self.matrix[node.y+1][node.x])
                        if self.inBoardBounds(node.x, node.y-1):
                            queue.appendleft(self.matrix[node.y-1][node.x])
                        if self.inBoardBounds(node.x+1, node.y):
                            queue.appendleft(self.matrix[node.y][node.x+1])
                        if self.inBoardBounds(node.x-1, node.y):
                            queue.appendleft(self.matrix[node.y][node.x-1])
            for capNode in searched:
                capNode.searched = False
                capNode.setEmpty()
    
    def zeroLiberties(self, x, y, player):
        node = self.matrix[y][x]
        queue = deque([node])
        searched = []
        while len(queue) > 0:
            node = queue.pop()
            if not node.searched:
                if node.isEmpty():
                    for capNode in searched:
                        capNode.searched = False
                    return False
                if node.piece != player:
                    node.searched = True
                    searched.append(node)
                    if self.inBoardBounds(node.x, node.y+1):
                        queue.appendleft(self.matrix[node.y+1][node.x])
                    if self.inBoardBounds(node.x, node.y-1):
                        queue.appendleft(self.matrix[node.y-1][node.x])                        
                    if self.inBoardBounds(node.x+1, node.y):
                        queue.appendleft(self.matrix[node.y][node.x+1])
                    if self.inBoardBounds(node.x-1, node.y):
                        queue.appendleft(self.matrix[node.y][node.x-1])
        for capNode in searched:
            capNode.searched = False
        return True
    
    def checkCaptures(self, x, y):
        self.evalLiberties(x-1, y, self.playing)
        self.evalLiberties(x+1, y, self.playing)
        self.evalLiberties(x, y-1, self.playing)
        self.evalLiberties(x, y+1, self.playing)
    
    def checkClick(self, x, y):
        if self.inPosBounds(x, y):
            xNode, yNode = self.getNodes(x, y)
            node = self.matrix[yNode][xNode]
            if node.isEmpty():
                if self.playing == "b":
                    node.setBlack()
                elif self.playing == "w":
                    node.setWhite()
                #if self.zeroLiberties(xNode, yNode, self.playing):
                #    node.setEmpty()
                #else:
                self.checkCaptures(xNode, yNode)
                self.changePlayer()
    
    
    
    
    
    
    
    
    
    
    
    
from Constants import *

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None
        
        self.searched = False
    
    def showEllipse(self, xPos, yPos):
        ellipse(xPos + CELLDIM // 2, yPos + CELLDIM // 2, CELLDIM-1, CELLDIM-1)
    
    def isEmpty(self):
        return self.piece == None
    
    def isBlack(self):
        return self.piece == "b"
    
    def isWhite(self):
        return self.piece == "w"
    
    def setBlack(self):
        self.piece = "b"
    
    def setWhite(self):
        self.piece = "w"
    
    def setEmpty(self):
        self.piece = None
    
    def getPos(self):
        return (MARGIN + self.x * CELLDIM, MARGIN + self.y * CELLDIM)
    
    def show(self):
        noStroke()
        fill(*CELLCOLOR)
        xPos, yPos = self.getPos()
        rect(xPos, yPos, CELLDIM, CELLDIM)
        stroke(0)
        if self.piece == "b":
            fill(*BLACKCOLOR)
            self.showEllipse(xPos, yPos)
        elif self.piece == "w":
            fill(*WHITECOLOR)
            self.showEllipse(xPos, yPos)
        else:
            stroke(*LINECOLOR)
            if self.y == 0:
                line(xPos+CELLDIM//2,yPos+CELLDIM//2,xPos+CELLDIM//2,yPos+CELLDIM)
            elif self.y == SIZE - 1:
                line(xPos+CELLDIM//2,yPos,xPos+CELLDIM//2,yPos+CELLDIM//2)
            else:
                line(xPos + CELLDIM // 2, yPos, xPos + CELLDIM // 2, yPos + CELLDIM)
            if self.x == 0:
                line(xPos+CELLDIM//2,yPos+CELLDIM//2,xPos+CELLDIM,yPos+CELLDIM//2)
            elif self.x == SIZE - 1:
                line(xPos,yPos+CELLDIM//2,xPos+CELLDIM//2,yPos+CELLDIM//2)
            else:
                line(xPos, yPos + CELLDIM // 2, xPos + CELLDIM, yPos + CELLDIM // 2)
            stroke(0)
    
    def showTransparent(self, side):
        if self.isEmpty():
            if side == "b":
                fill(*TRANSPARENTBLACK)
            elif side == "w":
                fill(*TRANSPARENTWHITE)
            xPos, yPos = self.getPos()
            self.showEllipse(xPos, yPos)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
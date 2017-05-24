from Constants import *
from Board import *

def setup():
    global b
    size(CANVASSIZE, CANVASSIZE)
    background(*BACKGROUND)
    b = Board()

def draw():
    b.show()
    b.checkHover(mouseX, mouseY)

def mousePressed():
    b.checkClick(mouseX, mouseY)
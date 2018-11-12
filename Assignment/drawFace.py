# drawFace.py
# A program that draw & color multiple faces
# by Tung Nguyen


from graphics import *

#create a graph win with length of x=500px, y=500px
win = GraphWin('Draw Faces', 500, 500)

#reset co-ord x,y to 0.0 && scale length of x,y to 5.0
win.setCoords(0, 0, 5.0, 5.0)

def drawFace(x , y, size, win):

    # create a point from 2 coordinates taken from user's input
    center = Point(x,y)

    # draw the face from the input point & size
    face = Circle(center, size)
    face.setFill('yellow')
    face.draw(win)

    # create 1st eye by cloning the face (size only 20%)
    eye1 = Circle(center, size*0.2)
    # move the 1st eye to the left && higher from the input center point
    eye1.move(0.15, 0.15)
    # actually draw the 1st eye in the window
    eye1.draw(win)

    # create 2nd eye by cloning the face (size only 20%)
    eye2 = Circle(center, size*0.2)
    # move the 2nd eye to the right && higher from the input center point
    eye2.move(-0.15, 0.15)
    # actually draw the 2nd eye in the window
    eye2.draw(win)

    # create a line by create 2 point to the left & right of the center point
    mouth = Line(Point(x-0.15, y-0.15), Point(x+0.15, y-0.15))
    # actually draw the line in the window
    mouth.draw(win)

def test():
    # draw face no.1 with Point(0.35, 1.5) & size = 0.35 
    drawFace(1.35, 1.5, 0.35, win)

    # draw face no.2 with Point(2.35, 3.05) & size = 0.45 
    drawFace(2.35, 3.05, 0.45, win)

    # draw face no.3 with Point(4.15, 4.15) & size = 0.55 
    drawFace(4.15, 4.15, 0.55, win)

test()

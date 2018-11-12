# drawTruck.py
# A program that draw & color a truck
# by Tung Nguyen


from graphics import *

def main():
    ### Open a graphics window && define width, height = 500px
    win = GraphWin('A truck', 500, 500)
    ### Set x & y to 0.0 && scale x, y to 5.0
    win.setCoords(0.0, 0.0, 5.0, 5.0)

    ### draw the truck body & fill the color with red
    body = Rectangle(Point(0.75,1.5), Point(4.25,3.5))
    body.setFill('Red')
    body.draw(win)
    
    ### draw the truck window & fill the color with white
    window = Rectangle(Point(3,2), Point(4.25,3.15))
    window.setFill('White')
    window.draw(win)

    ### draw the truck wheels & color them with black
    leftWheel = Circle(Point(1.35,1.5),0.35)
    leftWheel.setFill('black')
    rightWheel = leftWheel.clone()
    rightWheel.move(2.3,0)
    
    leftWheel.draw(win)
    rightWheel.draw(win)

main()

#clickexample.py
from graphics import *

def main():
    win = GraphWin("Click Me!", 500,500)

    #Introduce a loop for convenience
    for i in range(10):
        answer = input("Choose a circle (c) or rectangle (r):  ")
        if answer == "c":
            point = win.getMouse()
            radius = 20
            circle = Circle(point, radius)
            circle.draw(win)
            for i in range(5):
                win.getMouse()
                radius += 10
                circle = Circle(point,radius)
                circle.setOutline('blue')
                circle.draw(win)
        elif answer == "r":
            point1 = win.getMouse()
            point2 = win.getMouse()
            average1 = (point1.getX() + point2.getX()) - 2
            average2 = (point1.getY() + point2.getY()) - 2
            rectangle = Rectangle(point1, point2)
            rectangle.setFill('red')
            rectangle.draw(win)
            print("The center of your rectangle is", average1, average2)

        else:
            print("Invalid Input")            

    win.close()
main()

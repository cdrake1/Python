#move.py
from graphics import *
def main():
    win = GraphWin("Move!", 500, 500)
    circle = Circle(Point(50, 50), 20)
    circle.setFill('blue')
    circle.draw(win)

    key = win.getKey()
    print(key)
    while (key != 'q'):
        if key == 'r':
            circle.move(10, 0)
        elif key == 'l':
            circle.move(-10, 0)
        elif key == 'u':
            circle.move(0,-10)
        elif key == 'd':
            circle.move(0,10)
        elif key == 'p':
            circle.move(10,-10)
        elif key == 'z':
            circle.move(-10,10)
        elif key == 'm':
            circle.move(10,10)
        elif key == 'w':
             circle.move(-10,-10)
        elif key == 'c':
            point = win.getMouse()
            radius = 20
            circle = Circle(point, radius)
            circle.draw(win)
        elif key == 'e':
            point1 = win.getMouse()
            point2 = win.getMouse()
            rectangle = Rectangle(point1, point2)
            rectangle.draw(win)
        else:
            print("invalid key")
        key = win.getKey()
        print(key)
    win.close()


main()

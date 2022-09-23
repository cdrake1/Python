from graphics import *

def main():
    win = GraphWin("Click Me!", 500,500)
    point = win.getMouse()
    radius = 200
    circle = Circle(point, radius)
    num = int(input("How many circles do you want: "))
    for i in range(num):
        radius -= 25
        circle = Circle(point,radius)
        circle.draw(win)


main()
        
        

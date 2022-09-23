from graphics import *
def main():
    win = GraphWin("My graphics example", 500, 500)
    
    center = Point(250, 250)
    circle = Circle (center, 180)
    circle.setWidth(5)
    circle.setFill('grey')
    circle.draw(win)

    center2 = Point(170, 185)
    circle2 = Circle(center2, 28)
    circle2.setFill('black')
    circle2.draw(win)

    center3 = Point(330,185)
    circle3 = Circle(center3, 28)
    circle3.setFill('black')
    circle3.draw(win)

    line1 = Line( Point(140, 158),  Point(200,158))
    line1.setWidth(7)
    line1.draw(win)

    line2 = Line( Point(300,158), Point(360, 158))
    line2.setWidth(7)
    line2.draw(win)

    triangle1 = Polygon(Point(120,125), Point(80,20), Point(180,85))
    triangle1.setFill('grey')
    triangle1.setWidth(5)
    triangle1.setOutline('black')
    triangle1.draw(win)

    triangle2 = Polygon(Point(420,20), Point(320,85), Point(380,125))
    triangle2.setFill('grey')
    triangle2.setWidth(5)
    triangle2.setOutline('black')
    triangle2.draw(win)

    center4 = Point (250,270)
    circle4 = Circle (center4, 7)
    circle4.setFill('black')
    circle4.draw(win)

    oval1 = Oval( Point(290,300), Point(300,300))
    oval1.setWidth(7)
    oval1.draw(win)
    oval2 = Oval( Point(290,300), Point(250,300))
    oval2.setWidth(7)
    oval2.draw(win)

    oval3 = Oval( Point(210,300), Point(200,300))
    oval3.setWidth(7)
    oval3.draw(win)
    oval4 = Oval( Point(210,300), Point(250,300))
    oval4.setWidth(7)
    oval4.draw(win)

    line2 = Line( Point(250,270), Point(250,305))
    line2.setWidth(8)
    line2.draw(win)

    oval5 = Oval(Point(220,300), Point(280,370))
    oval5.setWidth(4)
    oval5.setFill('pink')
    oval5.draw(win)

main()

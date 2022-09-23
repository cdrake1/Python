#Snowman click
from graphics import *
def main():
    win = GraphWin("Move!", 500, 500)
    radius = int(input("Enter the radius for the snowmans body: "))
    point1 = win.getMouse()
    circle1 = Circle((point1),radius)
    x = point1.getX()
    radius1 = radius * 1.5
    y = point1.getY() 
    circle2 = Circle(Point(x, y), radius1)
    x1 = point1.getX()
    y1 = point1.getY() - 70
    radius2 = radius * 0.75
    circle3 = Circle(Point(x1, y1), radius2)
    
    hat1 = x1+20
    hat2 = y1 - 50
    hat3 = x1 -20
    hat4 = y1- 50
    rectangle1 = Rectangle(Point(hat1, hat2), Point(hat3, hat4))
    #rectangle2 = Rectangle(hat3, hat4)
    circle1.setFill('white')
    circle2.setFill('white')
    circle3.setFill('white')
    rectangle1.setFill('black')
    #rectangle2.setFill('black')
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    rectangle1.draw(win)
    #rectangle2.draw(win)
    rad = radius2 * 0.25
    eyex = x1 - 10
    eyey = y1 - 5
    eye2x = x1 +10
    eye2y = y1 - 5
    eye1 = Circle(Point(eyex, eyey), rad)
    eye2 = Circle(Point(eye2x, eye2y),rad)
    eye1.setFill('black')
    eye2.setFill('black')
    eye1.draw(win)
    eye2.draw(win)
    

main()
        
    
    
    

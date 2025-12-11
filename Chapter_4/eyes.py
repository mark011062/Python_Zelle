from graphics import *

leftEye = Circle(Point(80, 50), 5)
leftEye.setFill("yellow")
leftEye.setOutline("red")
rightEye = leftEye.clone()
rightEye.move(20, 0)    
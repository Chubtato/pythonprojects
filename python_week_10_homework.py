#!/usr/bin/python
#-----------------------------------------------------------------
# This program is a class of shapes
# Author: Paurush
#
# Date : 10/7/2017
#
# Version : 1.0
#
# copyright (C)
#-----------------------------------------------------------------

class Shape:
    """ Shape base class """
    def __init__(self, howManySides, area, perimeter):
        self.howManySides = howManySides
        self.area = area
        self.perimeter = perimeter

    def getHowManySides(self):
        return(self.howManySides)
    def getArea(self):
        return(self.area)
    def getPerimeter(self):
        return(self.perimeter)
    
class Square(Shape):
    def __init__(self, sideLength):
        self.howManySides=4
        self.sideLength = sideLength
        self.area = self.sideLength*self.sideLength
        self.perimeter = 4*self.sideLength

    def setSideLength(self, sideLength):
        self.sideLength = sideLength
        self.area = self.sideLength*self.sideLength
        self.perimeter = 4*self.sideLength

    def getSideLength(self):
        return(self.sideLength)
        
class Rectangle(Shape):
    def __init__(self, sideLength1, sideLength2):
        self.howManySides=4
        self.sideLength1 = sideLength1
        self.sideLength2 = sideLength2
        self.area = self.sideLength1*self.sideLength2
        self.perimeter = self.sideLength1+self.sideLength1+self.sideLength2+self.sideLength2

    def setSideLength1(self, sideLength):
        self.sideLength1 = sideLength
        self.area = self.sideLength1*self.sideLength2
        self.perimeter = (self.sideLength1*2)+(self.sideLength2*2)
    def setSideLength2(self, sideLength):
        self.sideLength2 = sideLength
        self.area = self.sideLength1*self.sideLength2
        self.perimeter = self.sideLength1+self.sideLength1+self.sideLength2+self.sideLength2

    def getSideLength1(self):
        return(self.sideLength1)

    def getSideLength2(self):
        return(self.sideLength2)

class Triangle(Shape):
    def __init__(self, sideLength1, sideLength2, sideLength3):
        self.howManySides=3
        self.sideLength1 = sideLength1
        self.sideLength2 = sideLength2
        self.sideLength3 = sideLength3
        self.perimeter = self.sideLength1+self.sideLength2+self.sideLength3

    def setSideLength1(self, sideLength):
        self.sideLength1 = sideLength
        self.perimeter = self.sideLength1+self.sideLength2+self.sideLength3

    def setSideLength2(self, sideLength):
        self.sideLength2 = sideLength
        self.perimeter = self.sideLength1+self.sideLength2+self.sideLength3

    def setSideLength3(self, sideLength):
        self.sideLength3 = sideLength
        self.perimeter = self.sideLength1+self.sideLength2+self.sideLength3

    def getSideLength1(self):
        return(self.sideLength1)

    def getSideLength2(self):
        return(self.sideLength2)

    def getSideLength3(self):
        return(self.sideLength3)
        
class Circle(Shape):
    def __init__(self, radius):
        self.howManySides=0
        self.radius = radius
        self.area = 3.14*self.radius*self.radius
        self.perimeter= 3.14*self.radius*2
    def setRadius(self, radius):
        self.radius = radius
        self.area = 3.14*self.radius*self.radius
        self.perimeter= 3.14*self.radius*2
    def getRadius(self):
        return(self.radius)
    def getArea(self):
        return(self.area)


c = Circle(4)
print(c.getArea())


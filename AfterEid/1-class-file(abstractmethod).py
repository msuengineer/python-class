from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noOfSides(self):
        pass
class Square(Polygon):
    def noOfSides(self):
        print('I have 4 sides') 
class Triangle(Polygon):
    def noOfSides(self): 
        print('I have 3 sides')

#a=Polygon()#error 
b=Square() 
b.noOfSides() 
c=Triangle() 
c.noOfSides()

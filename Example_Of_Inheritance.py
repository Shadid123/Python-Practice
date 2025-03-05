from abc import ABC,abstractmethod

class Shape():
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
        
    @abstractmethod
    def area(self):
        pass
        ###print("I am in shape class")
        
class Triangle(Shape):
    def area(self):
        result=0.5 * self.dim1 * self.dim2
        print("Area of Triangle is:",result)

class Rectangle(Shape):
    def area(self):
        result=self.dim1 * self.dim2
        print("Area of Rectangle is:",result)
    

Triangle=Triangle(20,30)
Rectangle=Rectangle(20,30)
Triangle.area()
Rectangle.area()
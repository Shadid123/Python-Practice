class Triangle:
    def __init__(self,height,base):
        self.height=height
        self.base=base
    def area(self):
        return 1/2*self.height*self.base
    def display(self):
        print("The area of triangle is:",self.area())


t1=Triangle(10,20)
t2=Triangle(30,40)
t1.display()
t2.display()
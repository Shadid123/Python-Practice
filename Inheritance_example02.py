class Bike:
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def __eq__(self,other):
        return  self.name==other.name and self.color==other.color
    def display(self):
        print(f"The color of the bike is:{self.color}\n The name of the bike is:{self.name}")
        
        
bike1=Bike("red","yamaha")
bike2=Bike("red","Suzuki")
bike1.display()
bike2.display()

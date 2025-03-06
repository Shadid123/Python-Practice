class Students:
    def __init__(self, name, id ,gpa):
        self.name=name
        self.id=id
        self.gpa=gpa
    def display(self):
        print(f"The id of {self.name} is:{self.id}\n The GPA of {self.name} is:{self.gpa}")


Shadid=Students("Shadid",25,3.50)
Shadid.display()
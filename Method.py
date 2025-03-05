class Student:
    name = ""
    id = ''
    gpa = ''

    def set_value(self, name, id, gpa):
        self.name = name  # Set the name of the student
        self.id = id      # Set the ID of the student
        self.gpa = gpa    # Set the GPA of the student

    def display(self):
        print(f"The id of {self.name} is: {self.id}")
        print(f"The GPA of {self.name} is: {self.gpa}")

# Create an instance of the Student class
Karim = Student()

# Set values for Karim
Karim.set_value("Karim", 25, 3.50)

# Display Karim's information
Karim.display()

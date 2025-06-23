class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.marks = marks
        try:
            if not isinstance(age, int) or age <= 0:            #isinstance(object, type) will check the type os the object is true or false.
                raise ValueError("Age should be a positive integer")
            self.age = age
        except ValueError as e:
            print(e)
    def calculate_grade(self):
        try:
            if not isinstance(self.marks, (int, float)):
                raise ValueError("Invalid input: Marks should be a number")
            if self.marks >= 90:
                return 'A'
            elif self.marks >= 80:
                return 'B'
            elif self.marks >= 70:
                return 'C'
            elif self.marks >= 60:
                return 'D'
            else:
                return 'F'
        except ValueError as e:
            print(e)
    def display_info(self):
        grade = self.calculate_grade()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {grade}")
 
# Example usage:
# Correct initialization and usage
student1 = Student("Alice", 20, 85)
student1.display_info()
 
# Invalid age
student2 = Student("Bob", -5, 75)
 
# Invalid marks
student3 = Student("Carol", 25, "eighty")
 
# Correct initialization but displaying with invalid marks
student4 = Student("David", 22, 92)
student4.marks = "ninety-two"
student4.display_info()
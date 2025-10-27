class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Student(Person):
    # Constructor overriding
    def __init__(self, name, student_id):
        super().__init__(name)  # calls parent constructor
        self.student_id = student_id
        print("Student constructor called")

# Example
s = Student("Alice", 101)

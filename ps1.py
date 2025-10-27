# Q2. 1. Student Result System • Create a base class Student with attributes name, roll_no. 
# • Create a derived class Result that adds marks in 3 subjects and computes the total and percentage.
#  •
#  Handle an exception if marks entered are negative or greater than 100.



class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class Result(Student):
    def __init__(self, name, roll_no, marks):
        super().__init__(name, roll_no)
        try:
            if any(m < 0 or m > 100 for m in marks):
                raise ValueError("Marks should be between 0 and 100")
            self.marks = marks
        except ValueError as e:
            print("Error:", e)
            self.marks = [0, 0, 0]
        self.total = sum(self.marks)
        self.percent = self.total / 3

    def show_result(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Total: {self.total}, Percentage: {self.percent:.2f}%")

# Test
r1 = Result("Amit", 101, [90, 85, 88])
r1.show_result()
r2 = Result("Rita", 102, [50, -10, 80])  # will raise error
r2.show_result()

# 4. Employee Payroll System 
# o Base class: Employee (name, emp_id, salary) 
# o Derived class: Manager, Developer  Override a method calculate_bonus() 
# o Use exception handling for invalid salary input (e.g., negative values). 
# o Raise a TypeError if non-numeric salary is entered. 5. Library Management 
# o Base class: LibraryItem (title, author) o Derived classes: Book, Magazine 
# o Raise a BookNotAvailableError if user tries to borrow an unavailable book.
#o Demonstrate try...except...finally to handle the borrowing process.


class Employee:
    def __init__(self, name, emp_id, salary):
        try:
            # Try converting to float — this ensures numeric type
            salary = float(salary)
            if salary < 0:
                raise ValueError("Salary cannot be negative")
            self.name = name
            self.emp_id = emp_id
            self.salary = salary
        except ValueError:
            print("Error: Salary must be a non-negative number")
            self.salary = 0
        except TypeError:
            print("Error: Invalid salary input type")
            self.salary = 0

    def calculate_bonus(self):
        return 0


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2


class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.1


# Test
m1 = Manager("Rahul", 1, 50000)
print("Manager Bonus:", m1.calculate_bonus())

d1 = Developer("Amit", 2, -30000)  # Negative salary handled
print("Developer Bonus:", d1.calculate_bonus())

d2 = Developer("Karan", 3, "abc")  # Non-numeric handled
print("Developer Bonus:", d2.calculate_bonus())

# 3. Vehicle Information o Base class: Vehicle (company, model) 
# o Derived class: Car (number of doors, fuel type) 
# o Derived class: Bike (engine capacity) 
# o Raise an exception if user enters an empty company name or invalid fuel type.

class Vehicle:
    def __init__(self, company, model):
        if not company:
            raise ValueError("Company name cannot be empty")
        self.company = company
        self.model = model

class Car(Vehicle):
    def __init__(self, company, model, doors, fuel_type):
        super().__init__(company, model)
        if fuel_type not in ("Petrol", "Diesel", "Electric"):
            raise ValueError("Invalid fuel type")
        self.doors = doors
        self.fuel_type = fuel_type

class Bike(Vehicle):
    def __init__(self, company, model, engine_cc):
        super().__init__(company, model)
        self.engine_cc = engine_cc

# Test
c1 = Car("Honda", "City", 4, "Petrol")
print(c1.__dict__)
# b1 = Bike("", "Yamaha", 150)  # Error: Empty company

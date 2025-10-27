class Customer:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def delivery_charge(self):
        return 50  # default delivery charge

    def show_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Order Amount: ₹{self.amount}")
        print(f"Delivery Charge: ₹{self.delivery_charge()}")
        print(f"Total Payable: ₹{self.amount + self.delivery_charge()}")
        print("--------------------")


class RegularCustomer(Customer):
    # inherits everything, same delivery charge
    pass


class PrimeCustomer(Customer):
    def __init__(self, name, amount, points):
        # constructor overriding (adds prime points)
        super().__init__(name, amount)
        self.points = points

    # method overriding
    def delivery_charge(self):
        return 0  # free delivery for prime customers

    # method overriding (adds prime points info)
    def show_details(self):
        print(f"Prime Customer: {self.name}")
        print(f"Order Amount: ₹{self.amount}")
        print(f"Prime Points: {self.points}")
        print(f"Delivery Charge: ₹{self.delivery_charge()}")
        print(f"Total Payable: ₹{self.amount + self.delivery_charge()}")
        print("--------------------")


# Example usage
r1 = RegularCustomer("Amit", 400)
p1 = PrimeCustomer("Priya", 800, 120)

r1.show_details()
p1.show_details()

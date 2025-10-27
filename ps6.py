# 6. E-commerce Order
#  o Base class: Product (name, price) 
# o Derived class: OrderItem adds quantity and calculates total cost.
#  o Raise an exception for:  Negative price or quantity 
#  Quantity > available stock do all these make it simple as easy to follow

class Product:
    def __init__(self, name, price, stock):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = price
        self.stock = stock

class OrderItem(Product):
    def __init__(self, name, price, stock, quantity):
        super().__init__(name, price, stock)
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            if quantity > stock:
                raise ValueError("Quantity exceeds available stock")
            self.quantity = quantity
        except ValueError as e:
            print("Error:", e)
            self.quantity = 0

    def total_cost(self):
        return self.price * self.quantity

# Test
item1 = OrderItem("Shoes", 2000, 10, 3)
print("Total Cost:", item1.total_cost())
item2 = OrderItem("Watch", 1500, 5, 10)  # Error: exceeds stock

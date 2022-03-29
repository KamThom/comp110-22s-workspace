"""Class and Object instantiation."""


class Pizza:
    """Models the idea of a pizza."""

    size: str 
    toppings: int 
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        self.size = size
        self.toppings = toppings
        
    def price(self, tax: float) -> float:
        total: float = 0.0

        if self.size == 'large':
            total += 10.0
        else:
            total += 8.0
        
        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0
        
        total *= tax

        return total


a_pizza: Pizza = Pizza("large", 3)

print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")
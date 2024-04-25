# Step 1: Define the base class Pizza
class Pizza:
    def __init__(self):
        self.price = 10  # Base price of the pizza

    def get_price(self):
        return self.price

# Step 2: Create a PizzaDecorator class
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_price(self):
        # Call the get_price method of the base class and add the cost of the decorator
        return self.pizza.get_price()

# Step 3: Create decorator classes for toppings
class PepperoniTopping(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 2  # Additional price for pepperoni topping

    def get_price(self):
        # Call the get_price method of the base class and add the cost of the decorator
        return super().get_price() + self.price

class MushroomTopping(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 1.5  # Additional price for mushroom topping

    def get_price(self):
        # Call the get_price method of the base class and add the cost of the decorator
        return super().get_price() + self.price

# Step 4: Instantiate a Pizza object and decorate it with toppings
pizza = Pizza()  # Create a base pizza
pizza_with_toppings = MushroomTopping(PepperoniTopping(pizza))  # Add mushroom and then pepperoni toppings

# Step 5: Test the program by printing the final price of the pizza after adding the toppings
print("Final Price of Pizza with Toppings:", pizza_with_toppings.get_price())

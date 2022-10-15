class Item:
    def __init__(self, name, price, quantity):
        # print(f"A new instance created: {name}")

        """
        We can now dynamically assign an attribute
        to every instance of the 'Item' class.
        This attribute shall be called
        'name'.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x * y


"""
Create two instances of the item class
"""
# item_one = Item("Phone")
# item_two = Item("Laptop")

"""
Now, fetch their names
"""
# print(item_one.name)
# print(item_two.name)

"""
Create two instances of the item class and 
    calculate their total prices
"""
item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)

calc1 = item1.calculate_total_price(item1.price,
                                    item1.quantity)
# print(calc1)

"""
Sometimes, we don't yet have enough data to describe
    an instance of the class. 
So, we can provide default values. This way, we are not 
    required to provide every attribute.
    
    See script 3
"""

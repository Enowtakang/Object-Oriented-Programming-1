class Item:
    def __init__(self, name="None",
                 price=0.0,
                 quantity=0.0):

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        """
        Here, we just use the already-defined
        attributes
        """
        return self.price * self.quantity


"""
Let's try:
"""
item1 = Item(price=100, quantity=5)
print(item1.calculate_total_price())

"""
Now, we sure don't want a negative number for price
    or quantity. 
    
    How do we solve this?
        We need to assert that the numbers are 
        positive (i.e., zero or more)
        
    
    See script 6 
"""

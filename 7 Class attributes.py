class Item:
    """
    Define a CLASS attribute
    """
    pay_rate = 0.8  # The pay rate after 20% discount

    def __init__(self,
                 name='None',
                 price=0.0,
                 quantity=0.0):
        """
        Run validations to the received arguments.
            - Provide your own assert error messages
        """
        assert price >= 0.0, f"\nThe price must not be less than zero. \n Your price is: {price}"
        assert quantity >= 0.0, f"\nThe quantity must not be less than zero. \n Your quantity is: {quantity}"

        # Assign to self object
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
Instantiate the class
"""
item1 = Item(price=100, quantity=5)
print(item1.calculate_total_price())

"""
(Side note: Use >> Ctrl + D << to duplicate any
        highlighted stuff)
        
Access the ClASS attribute from the CLASS itself, then
    access the class attribute from an INSTANCE of the
    CLASS.
    
"""
print(Item.pay_rate)    # Class itself
print(item1.pay_rate)   # Instance of the class

"""
The magic attribute: __dict__ shows you all the 
    attributes contained in an object. 
"""
print(Item.__dict__)
print(item1.__dict__)

"""
How do we apply the CLASS attribute?

See script 8
"""

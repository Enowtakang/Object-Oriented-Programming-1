class Item:
    def __init__(self,
                 name='None',
                 price=0.0,
                 quantity=0.0):

        """
        Run validations to the received arguments.
            - Provide your own assert error messages
        """
        assert price >= 0.0, f"The price must not be less than zero. \n Your input value is: {price}"
        assert quantity >= 0.0, f"The quantity must not be less than zero. \n Your input quantity is: {quantity}"

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
Let's try:
"""
item1 = Item(price=100, quantity=5)
print(item1.calculate_total_price())


"""
Consider an attribute which is going to 
be shared amongst ALL THE INSTANCES of the class
    (GLOBAL)
    - For example, you want to apply a discount sale to 
        all items. 
    - These types of attributes are called 
        CLASS ATTRIBUTES.
    - Up until now, we have been working with 
        INSTANCE attributes. 

A CLASS attribute is an attribute which belongs 
    to the CLASS itself. We can access this attribute
    from the class itself, and also from 
    any instance of the class.
    
    
    See script 7

"""


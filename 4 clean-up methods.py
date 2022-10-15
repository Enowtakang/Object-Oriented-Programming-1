class Item:
    def __init__(self, name=None,
                 price=None,
                 quantity=None):

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
Lets try:
"""
item1 = Item(price=100, quantity=5)
print(item1.calculate_total_price())

"""
Now, what if someone put in a wrong data type while
    instantiating an attribute in the 'Item' class?
    
    We should provide default values which have the
        data types that we want the attributes to
        specifically take: 
            - String defaults value for string datatype
            - Float default value for float and integer
                data type
    
    See script 5
"""

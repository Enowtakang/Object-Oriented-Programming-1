class Item:
    def __init__(self, name=None,
                 price=None,
                 quantity=None):
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
Define an instance of the 'Item' class which 
    has no specified attributes, then an instance 
    which only has a 'name' and a 'quantity'. 
"""
item1 = Item()
item2 = Item(name='Phone', quantity=5)
# print(item2.quantity, ' and', item1.name)

"""
Note: 
When ever you don't have all of the attributes at once,
    specify the attribute name, for which you are
    supplying a value, as shown in the instantiation
    of 'item2'.
"""
#------------------------------

"""
NOTE: 
        The fact that you set some attributes in the
        __init__() constructor, does not mean that
        you cannot add new attributes to a SPECIFIC
        INSTANCE. Example:  
"""
# Here, we have used none of the attributes in the
# constructor.
# We then added new attributes.
item_three = Item()
item_three.has_num_pad = False


"""
Now, check this out:
    we can design methods which do not need to receive
    any parameters.
    
    See script 4
"""

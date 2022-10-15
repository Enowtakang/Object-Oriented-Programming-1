"""
We define a new datatype called 'Item'
"""


class Item:
    def __init__(self):
        print(f"An instance created")

    def calculate_total_price(self, x, y):
        return x * y


"""
Next, we can make an instance 
    of this 'Item' datatype
"""
item1 = Item()

"""
We can also assign attributes to the 
    above instance of the 'Item' datatype
"""
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

"""
Let us now see how to create some METHODS 
    and execute them on our instances.
    
    These methods would be accessible to our
        instances.
    Check out the 'calculate total price' method 
        in the 'Item' class above
"""
item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

# aaa = item2.calculate_total_price(item2.price,
#                                   item2.quantity)
# print(aaa)

"""
At this point, we see that everytime we instantiate 
    the 'Item' class, we need to hard code the 
    attributes.
What if we forget to hard code an attribute and at 
    some later point, the program stops working?
To solve this, we need to MAKE THE ATTRIBUTES part of 
    the 'Item' class, such that upon creating any 
    instance of this class, we are forced to provide
    information regarding the attribute values for that
    instantiation.

We achieve this using the __init__() constructor, as 
    shown in the 'Item' class above.
    
    (Continue on script 2)
    
"""

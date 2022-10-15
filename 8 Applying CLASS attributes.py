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

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        return self.price


"""
Instantiate the class
Apply discount
check if it has had an effect on price
"""
item1 = Item(price=100, quantity=5)
item1.apply_discount()
# print(item1.price)

"""
Note that the above discount (0.8) is used by all 
    instances of the Item class.
Consider that you wanted to have a different
    discount for a particular item.
    
    How do you give it its own specific discount?
    See how nicely done it 
"""
item2 = Item(name='Laptop', price=1000)

# For this instance, we shall specify a different
# discount - 0.7, instead of the 0.8 value which is
# available for all.
item2.pay_rate = 0.7

item2.apply_discount()
print(item2.price)

"""
We notice that the attempt to override the pay_rate
from the instance level did not work.
We need to go back to the 'apply_discount' method
    and change 'Item.pay_rate' to 'self.pay_rate'
    
    See the implementation in script 9
"""

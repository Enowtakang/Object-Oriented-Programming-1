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
        self.price = self.price * self.pay_rate
        return self.price


"""
For this instance, we shall specify a different
    discount : 0.7, instead of the 0.8 value 
    which is available for all as a CLASS attribute.
"""
item2 = Item(name='Laptop', price=1000)
item2.pay_rate = 0.7    # Specify different discount
item2.apply_discount()
print(item2.price)

"""
- Instantiate the class
- Apply discount
- Check if it has had an effect (using 0.8, 
    pay_rate, since we did not override the 
    class attribute value) on price
"""
item1 = Item(price=100, quantity=5)
item1.apply_discount()
print(item1.price)


"""
Move to script 900 ( for github purposes :)  )
"""

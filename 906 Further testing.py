import csv


class Item:
    """
    Define a CLASS attribute called 'pay_rate'
    Define an empty list attribute called 'all'
    """
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

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

        """
        Assign to self object
        """
        self.name = name
        self.price = price
        self.quantity = quantity

        """
        Actions to execute:
        1./ Append all instance attributes to the 
            'all' class attribute. 
        """
        Item.all.append(self)

    def calculate_total_price(self):
        """
        Here, we just use the already-defined
        attributes
        """
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        path = 'items.csv'
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                # we specify 'float()' below, because
                # it would naturally be read as
                # a string otherwise.
                # ALWAYS use FLOAT instead of INT!!!
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )

    """
    Our first static method:
    A static method is just a regular function!
    """
    @staticmethod
    def is_integer(num):
        """
        Here, we want to find out if a number has a
            decimal point in it.
        We count out the floats that are point zero
            e.g. 5.0, 10.0, etc
        We shall use the 'isinstance()' built-in
            function to check
        """
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"


class Phone(Item):

    def __init__(self,
                 name='None',
                 price=0.0,
                 quantity=0.0,
                 # Add the new attribute
                 broken_phones=0.0):
        """
        Call the super function in order to have
            access to all attributes and methods
            of the parent class.

        """
        super().__init__(
            # State the names of the attributes
            # in the PARENT class.
            name, price, quantity)
        """
        Run validations to the NEW attribute.
            - Provide your own assert error message
        """
        assert broken_phones >= 0.0, f"\nThe number of broken_phones must not be less than zero. \n Your number is: {broken_phones}"
        """
        Assign the NEW attribute to the 
            self object
        """
        self.broken_phones = broken_phones


# phone1 = Item('MTN Phone', 5000, 5)
phone2 = Phone('MTN Phone', 5000, 5,
               broken_phones=1)

"""
Let us print the following:
"""
print(Item.all)
print(Phone.all)

"""
We see that both results list the class as Item,
    even though one of the classes is Phone.
    
    We have solved this by replacing 
            Item(...
    in __repr__     to:
            {self.__class__.__name__}(...
    
"""


"""
Up until now, we have done everything 
    in the same file.
    
    It would be good to place each class in its own 
    FILE
    
    Let's see:
    
    item.py and phone.py
    
    We then use the classes in a 
        python script (907), ever so effortlessly
"""

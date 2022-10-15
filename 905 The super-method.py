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
        return f"Item({self.name}, {self.price}, {self.quantity})"


class Phone(Item):
    all = []

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

        """
        Actions to execute:
        1./ Append all instance attributes to the 
            'all' class attribute. 
        """
        Phone.all.append(self)


phone1 = Phone('MTN Phone', 5000, 5,
               broken_phones=1)

print(phone1.calculate_total_price())

"""
Further testing:

See script 906
"""

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
        # Prevent 'name' attribute from being edited
        # outside this class, ONCE IT HAS BEEN SET in
        # an Instance of the class.
        # The job is completed in the read-only
        # @property decorator below
        self.__name = name

        # The rest are okay
        self.price = price
        self.quantity = quantity

        """
        Actions to execute:
        1./ Append all instance attributes to the 
            'all' class attribute. 
        """
        Item.all.append(self)

    # Use a @property decorator to set the 'name'
    # attribute as read-only.
    @property
    def name(self):
        return self.__name

    # Overriding @property decorator using
    # a setter decorator
    @name.setter
    def name(self, value):
        if len(value) > 20:
            raise Exception('The name is too long!.')
        else:
            self.__name = value

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

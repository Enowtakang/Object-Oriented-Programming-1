from item import Item


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

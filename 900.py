"""
- Consider that we have so many instances
    which have been created.
- How can we know all of them at once?

- The idea is to (as shown below):
    1./ create an empty list as a CLASS attribute
        called 'all',
    2./ then append all the instance attributes to
        this class attribute in the __init__ constructor
"""


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

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"


"""
Create 5 instances
"""
item1 = Item(name='Phone', price=100, quantity=5)
item2 = Item(name='Laptop', price=1000, quantity=3)
item3 = Item(name='Cable', price=10, quantity=5)
item4 = Item(name='House', price=50, quantity=5)
item5 = Item(name='Keyboard', price=75, quantity=5)

"""
Lets see how many instances of our class 
    are there:
"""
number_of_instances = len(Item.all)
# print(number_of_instances)

"""
What are the names of all the instances 
    of the Item class?
"""
for instance in Item.all:
    print(instance.name)

"""
When we just print:     Item.all    , 
    we see weird stuff. 
We can solve this by using a magic method: __repr__
    which stands for represent, 
    then customize it such that printing:   Item.all
    would result in a desired output,
    
    AS SHOWN ABOVE

Lets test:
"""
print(Item.all)


"""
Since the actual class INSTANCES and CODE 
    are maintained in the same script, there
    is a problem:
        if we add more instance attributes to the 
        class, we must go and update ALL previously
        created attributes. 
        
        TERRIBLE
        
        How do we solve this?
        
        We can store the data in a DATABASE.
        (Assignment: Do this)
        
        But let's first try with CSV files.
        
        We created an items.csv() file to store all the 
        instances.
        
        In the next script, we shall instantiate the 
            CLASS using data from the .csv() file
        
        Over to script 901
"""

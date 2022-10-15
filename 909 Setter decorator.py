"""
Even though the @property decorator prohibits attribute
    change when set, we can still override it.

    We do this using an:
                @[attribute].setter decorator
"""
from item import Item


item1 = Item(name='Data', price=200)
item1.name = 'Base'
print(item1.name)

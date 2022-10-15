from item import Item


"""
In the example code below, we override the name
    which was given to the Item instance at the 
    moment of its creation.
"""
item1 = Item(name='Data', price=200)
# item1.name = 'Base' # refused to even set another name
print(item1.name)

"""
The above action may not be favorable at all times.
    It may not always be a good idea to change the 
    NAME of something at will.
    
    We need to do stuff in such a way that we are
        forced to go back to the code line which 
        created the instance, before changing the 
        name.
        
        This blocking is called 
            Encapsulation
            
        We use the '@property' decorator while
        working in the item.py file.
        
        How do we set the 'name' attribute 
        to be immutable?
"""


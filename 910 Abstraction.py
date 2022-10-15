"""
First summary:
    1./ Abstraction makes a method PRIVATE,
        i.e., inaccessible outside of the class.
    2./ Therefore, the method cannot be accessed
        at the instance level.
--------------------------------------------
Sometimes, you need to create a method in your
    class, in order to use it for the proper
    execution of another method.

    Therefore, it is important to make sure that
    the user cannot access this kind of method.

ABSTRACTION helps us hide these types of methods
    (which serve for the proper functioning of other
    methods) by placing a double underscore just before
    naming them.

    e.g.

    def __send_email():
        ...
        ...




"""
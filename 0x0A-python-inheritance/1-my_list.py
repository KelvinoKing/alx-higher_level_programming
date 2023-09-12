"""class MyList
the class inherits from list
"""


class MyList(list):
    """MyList class
    inherits from list class
    """
    def __init__(self):
        """class constructor"""
        pass

    def print_sorted(self):
        """ this method sorts a list
        and and stores it in a new list
        """
        print(sorted(self))

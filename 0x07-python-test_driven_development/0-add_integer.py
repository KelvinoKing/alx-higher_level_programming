def add_integer(a, b=98):
    """ Adds two integers and return result

    args:
        a : first parameter
        b : second parameter
    Raises:
        TypeError: if parameters are not integers or float
    Returns: result of addition
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    result = int(a) + int(b)
    return result

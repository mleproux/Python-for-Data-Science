def square(x: int | float) -> int | float:
    """Return the square of x"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the exponentiation of x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """Apply a function to an object when called and return the
     result of the arguments calculation."""
    count = 0

    def inner() -> float:
        """Call a function and return and store the result"""
        nonlocal count
        count = function(count)
        return count
    count = x
    return inner

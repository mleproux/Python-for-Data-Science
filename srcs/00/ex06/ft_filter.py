def ft_filter(function: any, iterable: any) -> any:
    """ft_filter(function or None, iterable) --> filter object\n
    Return an iterator yielding those items of iterable
    for which function(item) is true. \n
    If function is None, return the items that are true."""
    if function is None:
        return [i for i in iterable if i]
    return [i for i in iterable if function(i)]

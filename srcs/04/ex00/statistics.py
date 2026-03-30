def mean(args):
    """Calculate the mathematical average of the arguments"""
    return (sum(args) / len(args))


def median(args):
    """Calculate the median of the arguments"""
    mid = len(args) // 2
    return ((args[mid] + args[~mid]) / 2)


def quartile(args):
    """Calculate and return the first and last quartile of the arguments"""
    length = len(args)
    if length < 4:
        raise
    return ([float(args[int(length*(1/4))]), float(args[int(length*(3/4))])])


def variance(args):
    """Calculate the variance of the arguments"""
    deviations = [(x - mean(args)) ** 2 for x in args]
    return mean(deviations)


def standard_deviation(args):
    """Calculate the standard deviation of the arguments"""
    return variance(args) ** .5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Apply the keywords in kwargs to args and print the result
    - Print ERROR if keyword is invalid or calculation is impossible
    """
    sequence = list(args)
    sequence.sort()
    for value in kwargs.values():
        try:
            if args is None:
                raise
            if value == "mean":
                print(f"mean : {mean(sequence)}")
            elif value == "median":
                print(f"median : {median(sequence)}")
            elif value == "quartile":
                print(f"quartile : {quartile(sequence)}")
            elif value == "std":
                print(f"std : {standard_deviation(args)}")
            elif value == "var":
                print(f"var : {variance(args)}")
        except Exception:
            print("ERROR")

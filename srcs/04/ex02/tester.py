from callLimit import callLimit


@callLimit(3)
def f():
    """The mighty f function. Print f()."""
    print("f()")


@callLimit(1)
def g():
    """The mighty g function. Print g()."""
    print("g()")


for i in range(3):
    f()
    g()

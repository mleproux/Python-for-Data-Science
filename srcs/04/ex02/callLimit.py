def callLimit(limit: int):
    """Call a function or block the call if the limit threshold was reached"""
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if (count >= limit):
                print(f"Error: {function} call too many times")
                return
            count += 1
            function()
        return limit_function
    return callLimiter

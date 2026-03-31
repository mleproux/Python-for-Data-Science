import math


def NULL_not_found(object: any) -> int:
    object_type = type(object)
    if object is None:
        print(f"Nothing: {object} {object_type}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {object_type}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {object_type}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} {object_type}")
    elif isinstance(object, str) and object == "":
        print(f"Empty: {object_type}")
    else:
        print("Type not Found")
        return 1
    return 0

def all_thing_is_obj(object: any) -> int:
    object_type = type(object)

    if isinstance(object, int):
        print("Type not found")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {object_type}")
    else:
        print(f"{object_type.__name__} : {object_type}")
    return 42

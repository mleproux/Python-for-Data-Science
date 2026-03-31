from ft_filter import ft_filter


def is_char_lower(char):
    if char.islower():
        return True
    return False


def is_multiple_10(n):
    return (True if n % 10 == 0 else False)


def is_false(arg):
    return not arg


objects = (("g", "G", "g"),
           (True, False, True),
           (50, 32, 48, 80),
           ("", "not empty", "")
           )


def main():
    print("\t\t[!] FT_FILTER TEST [!]")
    print("-----------------------------------------------------------")
    print("\tfilter\t\t|\tft_filter")
    print("\t------\t\t|\t---------")
    # test 1
    result1 = list(filter(is_multiple_10, objects[2]))
    result2 = ft_filter(is_multiple_10, objects[2])
    print(result1, "\t\t|", result2)
    # test 2
    result1 = list(filter(is_char_lower, objects[0]))
    result2 = ft_filter(is_char_lower, objects[0])
    print(result1, "\t\t|", result2)
    # test 3
    result1 = list(filter(is_false, objects[1]))
    result2 = ft_filter(is_false, objects[1])
    print(result1, "\t\t|", result2)
    # test 4
    result1 = list(filter(is_false, objects[3]))
    result2 = ft_filter(is_false, objects[3])
    print(result1, "\t\t|", result2)
    # test 5
    result1 = list(filter(None, objects[1]))
    result2 = ft_filter(None, objects[1])
    print(result1, "\t\t|", result2)


if __name__ == "__main__":
    main()

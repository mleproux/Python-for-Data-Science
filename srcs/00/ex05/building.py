import sys


def print_infos(text) -> None:
    """Pring the necessary informations inside text argument: \n
    - The length
    - Number of uppercase character
    - Number of lowercase character
    - Number of punctuation marks
    - Number of white character
    - Number of digit
    """
    punc_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(f"The text contains {len(text)} characters:")
    print(f"{sum(c.isupper() for c in text)} upper letters")
    print(f"{sum(c.islower() for c in text)} lower letters")
    print(f"{sum(c in punc_marks for c in text)} punctuation marks")
    print(f"{sum(c.isspace() for c in text)} spaces")
    print(f"{sum(c.isdigit() for c in text)} digits")


def get_text() -> str:
    """Prompt the user to input a string"""
    text = None
    while text is None or len(text) == 0:
        text = input("Please, provide a string: ")
    return text


def main():
    """Print the characters informations inside text argument \n
    - #1: A string
    """
    text = None
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = get_text()
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)
    print_infos(text)


if __name__ == "__main__":
    main()

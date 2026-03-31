import sys
from ft_filter import ft_filter


def parse_args() -> int:
    """Parse the arguments inside sys.argv\n
        - 2 arguments is required
        - argument 1 must be a string
        - argument 2 must be a integrer
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        try:
            return int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        exit(1)


def main():
    """Print the words that have a length greater than \n
    - #1: A string
    - #2: An int to filter #1
    """
    number = parse_args()
    texts = sys.argv[1].split()
    result = ft_filter(lambda text: len(text) > number, texts)
    print(result)


if __name__ == "__main__":
    main()

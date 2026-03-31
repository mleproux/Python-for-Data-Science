import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provide"
    if (len(sys.argv) == 2):
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        result = "Even" if number % 2 == 0 else "Odd"
        print(f"I'm {result}!")
except AssertionError as error:
    print(AssertionError.__name__ + ":", error)

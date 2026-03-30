class calculator:
    def __init__(self, object) -> None:
        self.object = object

    def __add__(self, object) -> None:
        self.object = [i + object for i in self.object]
        self.print_result()

    def __mul__(self, object) -> None:
        self.object = [i * object for i in self.object]
        self.print_result()

    def __sub__(self, object) -> None:
        self.object = [i - object for i in self.object]
        self.print_result()

    def __truediv__(self, object) -> None:
        try:
            self.object = [i / object for i in self.object]
            self.print_result()
        except ZeroDivisionError as error:
            print(f"{ZeroDivisionError.__name__}: {error}")

    def print_result(self):
        print(self.object)

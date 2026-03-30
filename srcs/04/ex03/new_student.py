import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random id of 15 lowercased characters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student informations including :
    - Name
    - Surname
    - Is actice (true by default)
    - A randomly generated id
    - A login using the first letter
    of the name concatened with the username"""
    name: str
    surname: str
    active: bool = field(default=True)
    id: str = field(init=False)
    login: str = field(init=False)

    def __post_init__(self):
        self.id = generate_id()
        self.login = f"{self.name[0]}{self.surname}"

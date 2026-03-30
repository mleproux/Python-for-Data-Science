from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)
print("-----")
try:
    Student(name="Edward", surname="agle", login="banane")
except TypeError as error:
    print(f"{TypeError.__name__}: {error}")

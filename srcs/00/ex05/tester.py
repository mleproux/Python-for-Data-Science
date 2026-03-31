from building import print_infos


obj_test = (
    "Bonjour",
    "Aurevoir",
    "Salut, Comment Tu Vas?",
    "0123456789",
    "tab=\tbackline=\nspace= ",
    "sifsdfsdfs54fsdf6sdgsdsd/f/sdfsdf/sd.f,s.d/f,sdfsdfsd64f66sd4fs65d4f",
    "Python 3.0, released in 2008, was a major revision that is not\
 completely backward-compatible with earlier versions. Python 2\
 was discontinued with version 2.7.18 in 2020."
            )


def main():
    print("===\tTEST\t===")
    for test in obj_test:
        print(f"input: {test}")
        print_infos(test)
        if obj_test[-1] != test:
            print("\n")


if __name__ == "__main__":
    main()

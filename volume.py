from area import area


def volume():
    cross_section = area("Shape of CS: ")
    height = float(input("Height: "))

    return height * cross_section


if __name__ == "__main__":
    print(volume())

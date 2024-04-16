from math import pi


def triangle_area() -> float:
    base = float(input("Base: "))
    height = float(input("Height: "))

    return 0.5 * base * height


def circle_area() -> float:
    radius = float(input("Radius: "))

    return pi * radius**2


def rectangle_area() -> float:
    length = float(input("Length: "))
    width = float(input("Width: "))

    return length * width


def area(prompt: str) -> float:
    shape = input(prompt).lower()

    if shape in ("triangle", "t"):
        area = triangle_area()
    elif shape in ("circle", "c"):
        area = circle_area()
    elif shape in ("rectangle", "square", "r", "s"):
        area = rectangle_area()
    else:
        return None

    return round(area, 7)


if __name__ == "__main__":
    print(area("Shape: "))

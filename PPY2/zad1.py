# Mikołaj Wieczorek s24697

import math


def main():
    print("input values for ax^2 + bx + c")
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    delta = math.sqrt((int(b) ** 2) + 4 * int(a) * int(c))

    delta_description = ""

    if delta < 0:
        delta_description = "smaller than zero"

    if delta == 0:
        delta_description = "equal to zero"

    if delta > 0:
        delta_description = "greater than zero"

    print("delta is", delta_description)


if __name__ == "__main__":
    main()

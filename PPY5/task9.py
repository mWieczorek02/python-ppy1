def main():
    a = float(input("input first side: "))
    b = float(input("input second side: "))
    c = float(input("input third side: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("error: all values should be positive.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("sides are pythagorean.")
    else:
        print("sides are not pythagorean.")


if __name__ == "__main__":
    main()

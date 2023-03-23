def display_squared_table(n, i=1, j=1):
    if i <= n:
        product = i * j
        print(f"{product}\t", end="")

        if j == n:
            print()
            display_squared_table(n, i + 1, 1)
        else:
            display_squared_table(n, i, j + 1)


def main():
    size = int(input("Enter the size of the table: "))
    display_squared_table(size)


if __name__ == "__main__":
    main()

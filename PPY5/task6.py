def main():
    num = int(str(input("input number: ")))

    if (num < 0):
        num = num * -1
    print(f"absolute value: {num}")


if __name__ == "__main__":
    main()

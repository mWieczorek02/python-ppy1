def main():
    start = int(input("input start of range: "))
    end = int(input("input end of range: "))
    sum = 0
    for number in range(start, end+1):
        if (number % 2 == 0):
            sum += number


if __name__ == "__main__":
    main()

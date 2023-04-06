def main():
    num = int(str(input("input number: ")))

    start = int(str(input("input start of range: ")))
    end = int(str(input("input end of range: ")))

    for i in range(start, end+1):
        print(i / num)


if __name__ == "__main__":
    main()

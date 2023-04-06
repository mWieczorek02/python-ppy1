def main():
    sum = 0
    i = 1
    while (i <= 100):
        if i % 2 != 0:
            sum += i
        i += 1

    print(sum)


if __name__ == "__main__":
    main()

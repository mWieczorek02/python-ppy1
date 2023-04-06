def main():
    height = 3
    width = 4
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height-1 or j == 0 or j == width-1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    print(f"area: {height*width}")
    print(f"circumference: {2*height + 2*width}")


if __name__ == "__main__":
    main()

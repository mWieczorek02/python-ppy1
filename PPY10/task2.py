import re


if __name__ == "__main__":
    text = "Programowanie w języku Python – od A do Z"

    split = re.split(" ", text)

    print(split)


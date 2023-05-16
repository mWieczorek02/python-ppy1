from random import sample
from string import ascii_letters

if __name__ == "__main__":
    five_letters = ''.join(sample(ascii_letters, 5))
    print(five_letters)

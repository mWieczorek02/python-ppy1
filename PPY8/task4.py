import random

HANGMANS = [
    '''
 -----
     |
     |
     |
    ===
    ''',
    '''
 -----
 o   |
     |
     |
    ===
    ''',
    '''
 -----
 o   |
 |   |
     |
    ===
    ''',
    '''
 -----
 o   |
/|   |
     |
    ===
    ''',
    '''
 -----
 o   |
/|\  |
     |
    ===
    ''',
    '''
 -----
 o   |
/|\  |
/    |
    ===
    ''',
    '''
 -----
 o   |
/|\  |
/ \  |
    ===
    '''
]

WORD_LIST = [
    "discover",
    "discuss",
    "discussion",
    "disease",
    "enjoy",
    "enough",
    "enter",
    "building",
    "business",
    "but",
    "buy",
    "call",
    "can",
    "cancer",
    "candidate",
    "capital",
    "explain",
    "eye",
    "face",
]


def print_word(word_dict):
    for d in word_dict:
        if d[1]:
            print(d[0], end='')
        else:
            print("_", end='')
    print()


def main():
    max_guesses = len(HANGMANS)
    word_to_guess = random.choice(WORD_LIST)
    word_to_guess_dict = []

    for letter in word_to_guess:
        word_to_guess_dict.append([letter, False])
    print_word(word_to_guess_dict)

    wrong_guesses = 0

    while True:
        if wrong_guesses >= max_guesses:
            print("You lost")
            return
        letter = input("input letter: ")
        contains = False
        for d in word_to_guess_dict:
            if d[0] == letter:
                d[1] = True
                contains = True
        if not contains:
            print(HANGMANS[wrong_guesses])
            wrong_guesses += 1
        print_word(word_to_guess_dict)


if __name__ == "__main__":
    main()

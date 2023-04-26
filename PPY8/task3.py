# Proszę napisać grę, w której komputer wybiera losowo słowo, które gracz musi odgadnąć.
# Komputer informuje gracza, ile liter znajduje się w wybranym słowie.
# Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera jest zawarta w tym słowie.
# Komputer może odpowiedzieć tylko "tak"lub "nie".Gracz musi odgadnąć słowo.
import random

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


def main():
    word_to_guess = random.choice(WORD_LIST)
    print(f"dlugosc slowa to: {len(word_to_guess)}")
    for i in range(min(len(word_to_guess), 5)):
        letter = input("zgadnij litere: ")
        if word_to_guess.__contains__(letter):
            print("TAK")
        else:
            print("NIE")
    guessed_word = input("zgadnij slowo: ")
    if guessed_word == word_to_guess:
        print("poprawnie odgadles slowo")
    else:
        print("niepoprawnie odgadles slowo")


if __name__ == "__main__":
    main()

# Prosze napisać skrypt, który liczy za użytkownika.
# Ma on umożliwić użytkownikowi wprowadzenie liczbypoczątkowej,
# liczby końcowej i wielkości odstępu między podanymi liczbami.

def main():
    start = int(input("podaj liczbe poczatkowa: "))
    end = int(input("podaj liczbe koncowa: "))
    step = int(input("podaj odstep miedzy liczbami: "))
    for i in range(start, end+1, step):
        print(i)


if __name__ == '__main__':
    main()
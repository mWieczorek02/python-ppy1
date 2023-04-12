# Napisz funkcję wypisującą liczby Catalana. Funkcja ta powinna umożliwić użytkownikowi wyświetlenie
# liczb Catalana parzystych, nieparzystych lub wszyskich mniejszych od liczby podanej w argumnecie. Domyślnie funkcja wyświetla wszystkie liczby.
# funckja (N, {p,n,a})

def catalan(n):
    if n == 0:
        return 1
    else:
        return (4 * n - 2) * catalan(n - 1) // (n + 1)


def catalan_numbers_helper(n, result):
    if n == 0:
        return result
    else:
        result.append(catalan(n - 1))
        return catalan_numbers_helper(n - 1, result)


def catalan_numbers(n):
    if n <= 1:
        return []
    else:
        result = []
        catalan_numbers_helper(n, result)
        return result[::-1]


def print_catalan(n, type):
    numbers = catalan_numbers(n)
    if type == "a":
        print(*numbers, sep=", ")
    if type == "n":
        print(*filter(lambda number: int(number) % 2 != 0, numbers), sep=", ")
    if type == "p":
        print(*filter(lambda number: int(number) % 2 == 0, numbers), sep=", ")


def main():
    number = int(input("input max num for catalan: "))
    type = input("input type of numbers {n,p,a}:")
    print_catalan(number, type)


if __name__ == "__main__":
    main()

"""
Napisz skrypt proszący użytkownika o podanie20liczb z zakresu od−20do20.
•Liczby zapisz w postaci listy.
•Wykonaj następujące operacje na liście:
1. utwórz kopię listy,
2. wyszukaj liczby pierwsze i utwórz z nich krotkę,
3. podnieś do potęgi2liczby podzielne przez2i utwórz z nich krotkę,
4. z pierwotnej listy wyszukaj liczby podzielne przez2i zamień je na literęA.
"""


def is_prime(num):
    flag = False
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

        # check if flag is True
        if flag:
            return False
        else:
            return True


def map_dividables(num):
    if int(num) % 2 == 0:
        return "A"
    else:
        return num


def main():
    user_input = input("input 20 numbers in range from -20 to 20: ")
    numbers = user_input.split(" ")
    if len(numbers) != 20:
        print("not 20 numbers")
        return
    out_of_range = list(filter(lambda num: int(num) > 20 or int(num) < -20, numbers))
    if out_of_range:
        print("some numbers are out of range")
        return
    list_copy = numbers.copy()

    primes = tuple(filter(lambda num: is_prime(int(num)), list_copy))
    divided_and_powered = tuple(map(lambda num: (int(num) / 2) ** 2, list_copy))
    numbers = list(map(lambda num: map_dividables(int(num)), numbers))

    print(primes)
    print(divided_and_powered)
    print(numbers)


if __name__ == "__main__":
    main()

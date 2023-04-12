# Napisz funkcję sprawdzającą, które z podanych w argumncie liczb są liczbami doskonałymi. Funckja możne
# przyjmować dowolną ilość arguemntów. W wyniku działania funkcji powinien powstać słownik w postaci
# liczba: True, liczba: False

def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0 and i != num:
            sum += i
    return sum == num


def check_numbers(*nums):
    number_dict = {}
    for num in nums:
        number_dict[num] = is_perfect(num)
    return number_dict


def main():
    values = check_numbers(1, 4, 6, 28)
    print(values)


if __name__ == "__main__":
    main()

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


def main():
    n = int(input("input number: "))

    print("Catalana numbers smaller than", n, "are:")
    print(*catalan_numbers(n), sep=" ")


if __name__ == "__main__":
    main()

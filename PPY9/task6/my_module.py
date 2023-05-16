def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def print_and_sort(n, type):
    count = 0
    index = 0
    arr = []
    while count < n:
        if index % 2 == 0 and index % 3 != 0:
            arr.append(index)
            print(str(index)+" ", end="")
            count += 1
        index += 1
    print("")
    if (type == "desc"):
        arr.sort(reverse=True)
    elif (type == "asc"):
        arr.sort(reverse=False)
    else:
        print("wrong type")
        return
    print(*arr, sep=", ")


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

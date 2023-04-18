# Napisz generator liczb pierwszych uzyskanych metodą sita Eratostenesa. Domyślnie generator wyświetla
# pierwszych 75 liczb pierwszych.
import math

def f(pair):
    _, val = pair
    return val

def sieve_of_eratosthenes(num):
    prime = {}
    for i in range(2, num + 1):
        prime[i] = True
    p = 2
    while p**2 <= num:
        if prime[p]:
            for i in range(p**2, num + 1, p):
                prime[i] = False
        p += 1
    l = dict(filter(f, prime.items()))
    print(*list(l), sep=", ")


def main():
    sieve_of_eratosthenes(75)


if __name__ == "__main__":
    main()

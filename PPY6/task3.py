# Napisz generator liczb pierwszych uzyskanych metodą sita Eratostenesa. Domyślnie generator wyświetla
# pierwszych 75 liczb pierwszych.
import math


def sieve_of_eratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, num + 1):
        if prime[p]:
            print(p)


def main():
    sieve_of_eratosthenes(75)


if __name__ == "__main__":
    main()

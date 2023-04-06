def main():
    before = (3.69, 4.5, 3.6, 4.0, 3.99, 3.59)
    after = (4.5, 5.5, 4.69, 4.99, 4.00)

    maxAfter = max(after)
    minCombined = min(min(before), min(after))
    avgBefore = sum(before)/len(before)
    avgAfter = sum(after)/len(after)

    print(f"najwyzsza cena po nalozeniu podatku: {maxAfter}")
    print(f"najniższa cena przed i po: {minCombined}")
    print(f"średnia przed podwyżką cen: {avgBefore}")
    print(f"średnia cena po dodaniu nowego podatku: {avgAfter}")


if __name__ == "__main__":
    main()

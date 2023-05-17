from collections import Counter

if __name__ == "__main__":
    items = ["YES", "NO", "NO", "YES", "EMPTY", "YES", "NO"]
    items_counter = Counter(items)

    print(items_counter.most_common())

import random

if __name__ == "__main__":
    random.seed(15)
    items = ["python", "java", "sql", "c++", "c"]
    random.shuffle(items)
    print(items)

import random

if __name__ == "__main__":
    random.seed(12)
    items = ["python", "java", "sql", "c++", "c"]

    print(random.choice(items))

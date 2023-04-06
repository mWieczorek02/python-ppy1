def main():
    tv_characters = {
        "walter": 0,
        "jesse": 0,
        "gustavo": 0,
        "mike": 0,
        "saul": 0,
    }

    for key, _ in tv_characters.items():
        tv_characters[key] = len(key)

    print(tv_characters)


if __name__ == "__main__":
    main()

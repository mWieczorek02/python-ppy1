if __name__ == "__main__":
    name = input("input name ")
    date_of_birth = input("input date of birth ")
    email = input("input email ")
    phone = input("input phone number ")
    tuple = (name, date_of_birth, email, phone)
    list = [name, date_of_birth, email, phone]
    dictionary = {"name": name, "date_of_birth": date_of_birth, "email": email, "phone": phone}

    print(tuple)
    print(list)
    print(dictionary)


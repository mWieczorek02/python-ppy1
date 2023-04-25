class Product:
    def __init__(self, id, name, quantity, price) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}, quantity: {self.quantity}, price: {self.price}"


def show_products(products):
    print(*products, sep="\n")


def add_product(products):
    product_id = input("input product id: ")
    name = input("input product name: ")
    quantity = input("input product quantity: ")
    price = input("input product price: ")
    products.append(Product(product_id, name, quantity, price))
    print("product added.")
    return products


def remove_product(products):
    num = int(input("input product number to delete: "))
    if num < 1 or num > len(products):
        print("invalid number.")
    else:
        products = filter(lambda p: p[0] != num, products)
        print("product deleted.")
    return products


def main(products):
    print("1. list all products")
    print("2. add new product")
    print("3. remove product")
    print("4. end program")
    choice = input("\ninput option: ")

    if choice == "1":
        show_products(products)
    elif choice == "2":
        products = add_product(products)
    elif choice == "3":
        products = remove_product(products)
    elif choice == "4":
        return
    else:
        print("wrong operation")
    main(products)


if __name__ == "__main__":
    main([])

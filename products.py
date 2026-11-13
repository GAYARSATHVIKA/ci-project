def search_product():
    products = ["Laptop", "Mobile", "Headphones"]

    name = input("Enter product name: ")

    if name in products:
        print("Product Available")
    else:
        print("Product Not Available")

search_product()
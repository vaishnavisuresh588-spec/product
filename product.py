def product_details(product_id, name, quantity, price):
    return (
        f"Product ID   : {product_id}\n"
        f"Product Name : {name}\n"
        f"Quantity     : {quantity}\n"
        f"Price        : {price}\n"
    )


if __name__ == "__main__":
    product_id = "P101"
    name = "Mouse"
    quantity = 10
    price = 500

    print(product_details(product_id, name, quantity, price))

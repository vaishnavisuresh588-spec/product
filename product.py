def product_details(product_id, name, quantity, price):
    return (
        f"Product ID   : {product_id}\n"
        f"Product Name : {name}\n"
        f"Quantity     : {quantity}\n"
        f"Price        : {price}\n"
    )


if __name__ == "__main__":
    product_id = "123467856"
    name = "iphone 17"
    quantity = 1
    price = 80000

    print(product_details(product_id, name, quantity, price))

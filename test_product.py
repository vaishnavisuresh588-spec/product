from product import product_details

def test_product_details():
    expected_output = (
        "Product ID   : P101\n"
        "Product Name : Mouse\n"
        "Quantity     : 10\n"
        "Price        : 500\n"
    )

    assert product_details("P101", "Mouse", 10, 500) == expected_output

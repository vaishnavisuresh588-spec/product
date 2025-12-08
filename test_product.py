from product import product_details

def test_product_details():
    expected_output = (
        "Product ID   : 123457656\n"
        "Product Name : iphone 17\n"
        "Quantity     : 1\n"
        "Price        : 80000\n"
    )

    assert product_details("123457656", "iphone 17", 1, 80000) == expected_output

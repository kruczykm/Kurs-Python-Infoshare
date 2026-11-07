def example_type_error() -> None:
    quantity = "5"
    unit_price = 12.5

    print("Przed poprawką quantity ma typ:", type(quantity).__name__)
    fixed_quantity = int(quantity)
    print("Po poprawce wynik:", fixed_quantity * unit_price)


def example_none_error() -> None:
    customer_id = None

    if customer_id is None:
        print("Customer ID is missing")
    else:
        print(customer_id.strip())

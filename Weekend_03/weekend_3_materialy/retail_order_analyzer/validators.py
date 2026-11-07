Order = dict[str, str | int | float | None]

MIN_VALID_QUANTITY = 1
MIN_VALID_PRICE = 0.0
UNKNOWN_CUSTOMER_ID = "UNKNOWN"
DEFAULT_COUNTRY = "Unknown"


def is_valid_quantity(quantity: int) -> bool:
    return quantity >= MIN_VALID_QUANTITY


def is_valid_price(unit_price: float) -> bool:
    return unit_price > MIN_VALID_PRICE


def is_return(quantity: int) -> bool:
    return quantity < 0


def normalize_customer_id(customer_id: str | None) -> str:
    if customer_id is None:
        return UNKNOWN_CUSTOMER_ID

    return customer_id.strip()


def normalize_country_name(country: str) -> str:
    normalized_country = country.strip()

    if normalized_country == "":
        return DEFAULT_COUNTRY

    return normalized_country.title()


def is_valid_order(order: Order) -> bool:
    quantity = int(order["quantity"])
    unit_price = float(order["unit_price"])

    return is_valid_quantity(quantity) and is_valid_price(unit_price)

try:
    from .validators import Order, is_valid_order
except ImportError:
    from InfoShare_AI_Python.Weekend_03.weekend_3_materialy.retail_order_analyzer.validators import Order, is_valid_order


def calculate_line_total(quantity: int, unit_price: float) -> float:
    return quantity * unit_price


def calculate_total_revenue(orders: list[Order]) -> float:
    total_revenue = 0.0

    for order in orders:
        if is_valid_order(order):
            quantity = int(order["quantity"])
            unit_price = float(order["unit_price"])
            total_revenue += calculate_line_total(quantity, unit_price)

    return total_revenue


def count_valid_orders(orders: list[Order]) -> int:
    valid_orders_count = 0

    for order in orders:
        if is_valid_order(order):
            valid_orders_count += 1

    return valid_orders_count

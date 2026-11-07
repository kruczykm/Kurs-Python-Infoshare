from InfoShare_AI_Python.Weekend_03.order_analyzer.type_aliases import Orders
from InfoShare_AI_Python.Weekend_03.order_analyzer.validators import is_valid_order


def calculate_line_total(quantity: int, unit_price: float) -> float:
    return quantity * unit_price

def calculate_total_revenue(orders: Orders) -> float:
    total_revenue = 0.0

    for order in orders:
        if is_valid_order(order):
            quantity = int(order["quantity"])
            price = float(order["unit_price"])
            total_revenue += calculate_line_total(quantity, price)

    return total_revenue




















# NOTATKA Z ZAJEC 

# orders_raw = [
#     {"invoice_no": "536365", "stock_code": "85123A", "description": "WHITE HANGING HEART T-LIGHT HOLDER", "quantity": "6", "unit_price": "2.55", "customer_id": "17850", "country": "United Kingdom"},
#     {"invoice_no": "536366", "stock_code": "71053", "description": "WHITE METAL LANTERN", "quantity": "-1", "unit_price": "3.39", "customer_id": "17850", "country": "United Kingdom"},
#     {"invoice_no": "536367", "stock_code": "84406B", "description": "CREAM CUPID HEARTS COAT HANGER", "quantity": "8", "unit_price": "0", "customer_id": "17850", "country": "France"},
#     {"invoice_no": "536368", "stock_code": "84029G", "description": "KNITTED UNION FLAG HOT WATER BOTTLE", "quantity": "3", "unit_price": "3.39", "customer_id": None, "country": "Germany"},
#     {"invoice_no": "536369", "stock_code": "22752", "description": "SET 7 BABUSHKA NESTING BOXES", "quantity": "2", "unit_price": "7.65", "customer_id": "13047", "country": "United Kingdom"}
# ]

# Sprawdzenie zmiennej wbudowanej __name__ w module validators.py
# Wyswietli sie __main__ tylko wtedy, gdy uruchomimy ten plik bezposrednio, a nie jako import w innym module
# Gdy uruchomimy ten modul jako import w innym module, wyswietli sie nazwa tego modulu, czyli pricing
# print("print z pricing.py: ", __name__)

# if __name__ == "__main__":
#     line_total = calculate_line_total(3, 10.0)
#     print(line_total)
    # print(calculate_total_revenue(orders_raw))
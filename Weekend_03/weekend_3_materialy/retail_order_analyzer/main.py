from InfoShare_AI_Python.Weekend_03.weekend_3_materialy.retail_order_analyzer.pricing import calculate_total_revenue, count_valid_orders
from InfoShare_AI_Python.Weekend_03.weekend_3_materialy.retail_order_analyzer.reports import print_revenue_report


orders = [
    {"invoice_no": "536365", "quantity": "6", "unit_price": "2.55", "customer_id": "17850", "country": "United Kingdom"},
    {"invoice_no": "536366", "quantity": "-1", "unit_price": "3.39", "customer_id": "17850", "country": "United Kingdom"},
    {"invoice_no": "536367", "quantity": "8", "unit_price": "0", "customer_id": "17850", "country": "France"},
    {"invoice_no": "536368", "quantity": "3", "unit_price": "3.39", "customer_id": None, "country": "Germany"},
]


def main() -> None:
    total_revenue = calculate_total_revenue(orders)
    valid_orders_count = count_valid_orders(orders)
    print_revenue_report(total_revenue, valid_orders_count)


if __name__ == "__main__":
    main()

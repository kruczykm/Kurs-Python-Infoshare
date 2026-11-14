from pricing import calculate_total_revenue
from reports import print_revenue_report

# Alisy mozna tez tworzyc w ten sposob
type Order = dict[str, str]
type Orders = list[Order]

orders: Orders = [
    {"invoice_no": "536365", "quantity": "6", "unit_price": "2.55", "country": "United Kingdom"},
    {"invoice_no": "536366", "quantity": "-1", "unit_price": "3.39", "country": "United Kingdom"},
    {"invoice_no": "536367", "quantity": "8", "unit_price": "0", "country": "France"},
]


def main() -> None:
    total_revenue = calculate_total_revenue(orders)
    print_revenue_report(total_revenue)


if __name__ == "__main__":
    main()








# from pricing import calculate_line_total
# from validators import is_valid_quantity, is_valid_price

# Sprawdzenie zmiennej wbudowanej __name__ w module validators.py
# Wyswietli sie __main__ tylko wtedy, gdy uruchomimy ten plik bezposrednio, a nie jako import w innym module
# poniewaz __name__ domyslnie przyjmuje wartosc "__main__" tylko wtedy, gdy plik jest uruchamiany bezposrednio, 
# a gdy jest importowany, __name__ przyjmuje nazwe modulu.
# print("print z main.py: ", __name__)





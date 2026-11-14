# importuje nasz ALias
from type_aliases import Order

MIN_VALID_QUANTITY = 1
MIN_VALID_PRICE = 0.0
UNKNOWN_CUSTOMER_ID = "Unknown"


def is_valid_quantity(quantity: int) -> bool:
     return quantity >= MIN_VALID_QUANTITY

def is_valid_price(price: float) -> bool:
     return price > MIN_VALID_PRICE

def is_return(quantity: int) -> bool:
    return quantity < MIN_VALID_QUANTITY

def is_valid_order(order: Order) -> bool:
     quantity = int(order["quantity"])
     price = float(order["unit_price"]) 
     return is_valid_quantity(quantity) and is_valid_price(price)























# NOTATKA Z ZAJEC 

# to jest Alias mozna go uzywac przy pisaniu Typehint, lepiej trzymaj takie aliasy w oddzielnym pliku np.types.py
# Order = dict[str, str | float | int]

# Sprawdzenie zmiennej wbudowanej __name__ w module validators.py
# Wyswietli sie __main__ tylko wtedy, gdy uruchomimy ten plik bezposrednio, a nie jako import w innym module\
# Gdy uruchomimy ten modul jako import w innym module, wyswietli sie nazwa tego modulu, czyli validators
# print("print z validators.py: ", __name__)

# Ten warunek if __name__ == "__main__": pozwala na uruchomienie testów tylko wtedy, gdy uruchomimy ten plik bezposrednio, a nie jako import w innym module.
# Wyswietli sie __main__ tylko wtedy, gdy uruchomimy ten plik bezposrednio, a nie jako import w innym module
# poniewaz __name__ domyslnie przyjmuje wartosc "__main__" tylko wtedy, gdy plik jest uruchamiany bezposrednio, 
# a gdy jest importowany, __name__ przyjmuje nazwe modulu..
# if __name__ == "__main__":
#       print(is_valid_quantity(5))
#     print(is_valid_quantity(0))
#     print(is_valid_quantity(-3))
#     print(is_valid_quantity(10.45))
#     print(is_valid_quantity(0))
#     print(is_valid_quantity(-5.34))

# -----------------------------------------------------------------------------
# ZADANIE 6 – RABAT
# -----------------------------------------------------------------------------
#
# Napisz funkcję:
#
# calculate_final_price(price, customer_type)
#
#
# customer_type == "premium"
# -> rabat 20%
#
#
# customer_type == "standard"
# -> rabat 10%
#
#
# pozostałe wartości:
# -> brak rabatu
#
#
# Funkcja powinna ZWRACAĆ cenę po rabacie.
#
#
# Przykład:
#
# calculate_final_price(100, "premium")
#
# powinno zwrócić:
#
# 80.0

def calculate_final_price(price: float, customer_type: str) -> float:
    if customer_type == "premium":
        return price - price * 0.2
    elif customer_type == "standard":
        return price - price * 0.1
    else:
        return price

print(calculate_final_price(100, "premium"))
print(calculate_final_price(153.5, "standard"))
print(calculate_final_price(88.5, "normal"))

print("#########################################")

# bardziej Pajtonowo
def calculate_final_price_2(price: float, customer_type: str) -> float:
    if customer_type == "premium":
        discount = 0.2
    elif customer_type == "standard":
        discount = 0.1
    else:
        discount = 0
        
    return price * (1 - discount)

print(calculate_final_price_2(100, "premium"))
print(calculate_final_price_2(153.5, "standard"))
print(calculate_final_price_2(88.5, "normal"))
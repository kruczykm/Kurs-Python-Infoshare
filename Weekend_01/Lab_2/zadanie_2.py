# -----------------------------------------------------------------------------
# ZADANIE 2 – DARMOWA DOSTAWA
# -----------------------------------------------------------------------------
#
# Klient otrzymuje darmową dostawę, jeżeli:
#
# wartość zamówienia wynosi co najmniej 200 PLN
#
# LUB
#
# klient jest klientem premium.
#
#
# Jeśli warunek jest spełniony:
#
# "Darmowa dostawa"
#
#
# W przeciwnym przypadku:
#
# "Koszt dostawy: 15 PLN"
order_value = 150
is_premium = True

if order_value >= 200 or is_premium:
    print("Darmowa dostawa.")
else:
    print("Koszt dostawy: 15 PLN.")

'''
def check_cost_delivery(order_value: float, is_premium: bool):
    if order_value >= 200 or is_premium:
        print("Darmowa dostawa.")
    else:
        print("Koszt dostawy: 15 PLN.")

check_cost_delivery(265.5, True)    # Darmowa dostawa - oba warunki True
check_cost_delivery(200, False)    # Darmowa dostawa - pierwszy warunek True
check_cost_delivery(144.5, True)    # Darmowa dostawa - drugi warunek True
check_cost_delivery(144.5, False)    # Dostawa 15 PLN - oba warunki False
'''

# Zamiast powtarzać print w if i else:
def is_delivery_free(order_value: float, is_premium: bool) -> bool:
    print(f"Koszt twojego zamowienia to {order_value} PLN.")
    
    if order_value >= 200 or is_premium:
        return True
    else:
        return False

def check_cost_delivery(is_free_delivery: bool):
    if is_free_delivery:
        print("Darmowa dostawa.")
    else:
        print("Koszt dostawy: 15 PLN.")

check_cost_delivery(is_delivery_free(265.5, True))    # Darmowa dostawa - oba warunki True
check_cost_delivery(is_delivery_free(200, False))   # Darmowa dostawa - pierwszy warunek True
check_cost_delivery(is_delivery_free(144.5, True))   # Darmowa dostawa - drugi warunek True
check_cost_delivery(is_delivery_free(144.5, False))    # Dostawa 15 PLN - oba warunki False



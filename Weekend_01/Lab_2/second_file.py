'''

# konstrukcja warunkowa if ... else
age = 10

if age >= 18:
    print("Jesteś dorosły.")
    # ta linia wywola sie tylko jesli warunek jest prawdziwy
else:
    print("Jesteś nie pełnoletni.")
    # w każdym innym przypadku

# przyklad wyniki z matur
score = 75

if score >= 90:
    print("Poszło Ci bardzo dobrze.")
elif score >= 70:
    print("Udało Ci się zaliczyć.")
else:
    print("Brak zaliczenia.")

#AND
age = 25
has_ticket = True

if age >=18 and has_ticket: #True and True
    print('Mozna wejsc do kina')
else:
    print('Nie mozna wejsc')

#OR - lub - jeden z warunkow musi byc spelniony
city= 'Kraków'

if city =='Kraków' or city == 'Warszawa':
    print('Obsługujemy to miasto')
else:
    print('Nie obsługujemy tego miasta')

#alternatywa
if city in ['Kraków', 'Warszawa']:
    print('Obsługujemy to miasto')
else:
    print('Nie obsługujemy tego miasta')

#NOT - odwrocenie wartosci logicznej

is_blocked = False

if not is_blocked:
    print('dostep przyznany')

# Zadanie 1. Napisz taka instrukcje warunkowa, ktora przyznaje dostep, jesli ktos jest > 18; ma subkrypcje i nie jest zablkowany. Zadeklaruj samodzielnie zmienne.
age = 20
is_subscription = True
is_locked = False

if age >= 18 and is_subscription and not is_locked:
    print("Masz dostęp.")
elif age < 18:
    print("Jesteś nie pełnoletni.")
elif not is_subscription:
    print("Wykup subskrybcje.")
else:
    print("Jestes zablokowany.")

# if age >= 18 and is_subscription and not is_locked:
#     print("Masz dostęp.")
# else:
#     print("Nie masz dostępu.")


# Funkcje - cjcemy jakis fragment wywolac wiele razy
quantity = 100
price = 75
total = quantity * price
print(total)

# piszemy to samo tylko tworrzac funckje
def calculate_total(price: int, quantity: int):
    return price * quantity # return zwraca wartosc poza funckje - to jest wyjscie z funckje - return daje nam mozliwosc przypisania wartosci do zmiennej

print(calculate_total(100, 75))
print(calculate_total(100, 10))
print(calculate_total(120, 30))

def calculate_total_2(price: int, quantity: int):
    print(price * quantity) # tutaj mam wykonanie zadania

print(calculate_total_2(100, 75))
calculate_total_2(100, 75)
print(calculate_total_2(100, 75))
calculate_total_2(100, 10)
print(calculate_total_2(100, 75))
calculate_total_2(120, 30)

'''
def get_category(score: int):
    if score >= 80:
        return "high"
    elif score >= 50:
        return "medium"
    else:
        return "low"

print(get_category(100))
print(get_category(50))
print(get_category(-10))
## -----------------------------------------------------------------------------
# ZADANIE 1 – LICZBA DODATNIA, UJEMNA CZY ZERO
# -----------------------------------------------------------------------------
#
# Dana jest liczba:
#
# number = -10
#
# Napisz instrukcję if / elif / else.
#
# Program powinien wyświetlić:
#
# "Liczba jest dodatnia"
#
# jeśli number > 0
#
#
# "Liczba jest równa zero"
#
# jeśli number == 0
#
#
# "Liczba jest ujemna"
#
# w pozostałych przypadkach.

# number = -10
number = 0
# number = 10.5

if number > 0:
    print(f"Liczba {number} jest dodatnia.")
elif number == 0:
    print(f"Liczba {number} jest równa 0.")
else:
    print(f"Liczba {number} jest ujemna.")
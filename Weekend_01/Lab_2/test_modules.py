# importuje wszystkie funkcje z modulu test_modules.py
from test_functions import *
# importuje biblioteke statistic
import statistics as st
# a tu cos z pandas
import pandas as pd

print_name("Karolina")
name = return_name("Mateusz")
print(name)

# statistics - tylko go importujemy mozemy korzystac z wbudowanych funkcji
print(f"Srednia arytmetyczna liczba 1,2,3,4 to {st.mean([1,2,3,4])}.")

# pusta ramka danych
print(pd.DataFrame([]))


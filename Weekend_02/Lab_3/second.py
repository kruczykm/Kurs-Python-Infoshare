# Slownik w Pythonie to struktura danych, która przechowuje pary klucz-wartość. 
# Klucze muszą być unikalne, a wartości mogą być dowolnego typu danych. 
# Słowniki są używane do szybkiego wyszukiwania wartości na podstawie klucza.

nazwy_dni = {
    "Mon": "Poniedziałek",
    "Thu": "Czwartek",
    "Sat": "Sobota",
    "Wed": "Środa",
    "Tue": "Wtorek",
    "Fri": "Piątek",
    "Sun": "Niedziela",
    "Sat": "Sobotaaa",
}

# Dlaczego jest tak ze nadpisujemy klucze w słowniku? Ponieważ w słowniku klucze muszą być unikalne. 
# Jeśli dodamy nowy element z tym samym kluczem, poprzednia wartość zostanie nadpisana nową wartością. 
# W tym przypadku, klucz "Sat" został nadpisany z "Sobota" na "Sobotaaa".

print(nazwy_dni["Sat"])
      
working_days = {
    "Mon": "Poniedziałek",
    "Thu": "Czwartek",
    "Sat": "Sobota",
    "Wed": "Środa",
    "Tue": "Wtorek",
    "Fri": "Piątek",
    "Sun": None,
    "Sat": None,
}

weekend_days = {
    "Sun": "Niedziela",
    "Sat": "Sobotaaa",
}

# Łączenie dwóch słowników w jeden. 
# metody łączenia słowników w Pythonie 3.9 i nowszych:
# Trzeba pamiętać, że w przypadku konfliktu kluczy, wartość z ostatniego słownika nadpisze wartość z wcześniejszego słownika. Czyli jak w tym przypadku, 
# klucz "Sat" z weekend_days nadpisze wartość z working_days.

# 1. Użycie operatora **, który rozpakowuje zawartość słownika i tworzy nowy słownik z połączonymi elementami. 
# 2. Użycie metody update(), która aktualizuje słownik o elementy z innego słownika.
# 3. Użycie operatora |, który tworzy nowy słownik z połączonymi elementami.
# 4. Użycie funkcji chain() z modułu itertools, która łączy elementy z dwóch słowników w jeden iterator, a następnie tworzy nowy słownik z tych elementów.

names_of_days = {
    **working_days, 
    **weekend_days,
}

print(working_days)
print(weekend_days)
print(nazwy_dni)

# Wyciaganie wartości z słownika na podstawie klucza. 
# Metoda get() pozwala na ustawienie wartości domyślnej, która zostanie zwrócona, jeśli klucz nie istnieje w słowniku.
# Metoda get() jest bezpieczniejsza niż bezpośrednie odwołanie się do klucza, ponieważ nie spowoduje błędu, jeśli klucz nie istnieje. Tylko zwróci wartość domyślną, 
# którą możemy ustawić jako drugi argument metody get(), lub zwroci None, jeśli nie ustawimy wartości domyślnej.
# Czyli .get() to jest inwariant, który pozwala na bezpieczne pobieranie wartości z słownika, nawet jeśli klucz nie istnieje.

print(names_of_days.get("Mon", "Nie ma takiego dnia"))
print(names_of_days.get("Day")) # Zwroci None, bo nie ma takiego klucza w słowniku. Nie bedzie bledu jak w przypadku names_of_days["Day"]. 


#komentarz
# skrot do komentratrza - ctrl/cmd + "/"

# file.py - plik z .py rozszerzeniem poprwanie nazywa sie modułem
# zmianna - pozwala nam przechowywac wartosc pod okreslona nazwa 
# operator = przypisuje wartosc do zmiennej znajdujaca sie po prawej stronie do zmiennej po lewej

age = 35 # przypisanie do zmiennej age wartosci 35 (int)
print(age)
print(id(age))

name = zmienna = "Karolina" #zmienna przechowuje str
print(name)
print(age, name)

# nazwy zmiennych
# nie uzywamy uzywac spacji
# unikamy nazywania zmiennych tak jak elementy skladowe jezyka
# zmienne uzywamy zmalej litery duze zarezerwowane sa dla klas - wyjatki M,X jak bedziemy oznaczac macierze
# zmiennych nie zaczynamy od cyfr

# snake case
any_variable = 10
print(any_variable)

# Podstawowe typy danych
# STR - text
# INT - liczby calkowite
# FLOAT - zmiennoprzecinkowa
# Boolean - true/false
# None Type - brak wartosci None

# Czy istnieje najwiekszy integer w Pythonie? Nie, w Pythonie 3.x liczby całkowite mogą być dowolnie duże, ograniczone jedynie przez dostępną pamięć.

print(1+1)
print(1-5)
print(1*4) # mnozenie
print(4/4) # dzielenie wynik zawsze bedzie float
print(4//4) # dzielenie calkowite
print(4%3) # modulo reszta z dzielenia

number_1 = 10
number_2 = 15

# konwencja umownie dodjamey spacje przy operatorach matematycznych
print(number_1 + number_2) 

# czy istanieje najwiekszy float w Pythonie? Tak, 
# w Pythonie istnieje ograniczenie dla liczb zmiennoprzecinkowych (float), 
# które jest zależne od implementacji i architektury systemu. W praktyce, 
# float w Pythonie jest oparty na standardzie IEEE 754 i ma ograniczoną precyzję, co oznacza, że może reprezentować liczby w określonym zakresie.

g = 0.357437473743747347324372
print(g)

# float precision - precyzja floatow w Pythonie jest ograniczona, co oznacza, że nie wszystkie liczby zmiennoprzecinkowe mogą być reprezentowane dokładnie.
print(0.357437473743747347324372 == 0.357437473743747347324373) # wychodzi True bo float nie jest w stanie przechowywac takiej precyzji
print(0.1 + 0.1 + 0.1) # na samym koncu jest 0.30000000000000004 bo float nie jest w stanie przechowywac takiej precyzji

# Jak rozwiązać problem z precyzją floatów w Pythonie? Można użyć modułu decimal,  
#który pozwala na dokładniejsze operacje na liczbach zmiennoprzecinkowych, lub zaokrąglać wyniki do określonej liczby miejsc po przecinku.
print(round(0.1 + 0.1 + 0.1, 2)) # zaokraglenie do 2 miejsc po przecinku
# Aby użyć modułu `decimal` w Pythonie do precyzyjnych oblic zeń zmiennoprzecinkowych, 
# należy najpierw zaimportować go, a następnie używać klasy `Decimal` do reprezentowania liczb. Oto przykład:
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))  # Wynik: 0.3
print(Decimal('0.1') + Decimal('0.2'))  # Wynik: 0.3


# co to jest string? - jest to ciag znakow, w Pythonie stringi mozna zapisac uzywajac pojedynczych lub podwojnych apostrofow
name = 'Karolina'

# co to jest multiline string? - jest to string ktory zajmuje wiecej niz jedna linie kodu, 
# w Pythonie mozna go zapisac uzywajac potrojnych apostrofow lub potrojnych cudzyslowow
n = """To jest
multiline
string"""

# kontatenacja stringow - laczenie stringow
name = "Karolina"
surname = "Kowalska"
print(name + " " + surname) # laczenie stringow za pomoca operatora +

# mnozenie stringow - powielanie stringow
print(name * 3) # powielanie stringow za pomoca operatora *

#Boolean - typ danych ktory moze przyjmowac tylko dwie wartosci True lub False
is_student = True
is_admin = False

print(type(is_student)) # sprawdzenie typu danych zmiennej is_student
print(type(is_admin)) # sprawdzenie typu danych zmiennej is_admin

print(age > 18) # sprawdzenie czy zmienna age jest wieksza od 18

# operatory porownnania co to jest? - sa to operatory ktore pozwalaja nam porownywac wartosci zmiennych,
# w Pythonie sa to: ==, !=, >, <, >=, <=
print(age == 35) # sprawdzenie czy zmienna age jest rowna 35
print(age != 35) # sprawdzenie czy zmienna age jest rozna od 3
print(age > 18) # sprawdzenie czy zmienna age jest wieksza od 18
print(age < 18) # sprawdzenie czy zmienna age jest mniejsza od 18

# zmiany typu - konwersji typow
print(int(10.0)) # sprawdzenie typu danych zmiennej age

# sprobuj przekonwertowac np. 5 rownych kombinacji typow
print(int(10.5)) # konwersja float na int - wynik 10 bo float 10.5 jest konwertowany na int 10 ucinamy koncowke po przecinku
print(float(10.6)) # konwersja int na float - wynik 10 bo int 10 jest konwertowany na float 10.0
print(str(10)) # konwersja int na str - wynik "10" bo int 10 jest konwertowany na string "10"
print(float("10.5")) # konwersja float na str - wynik 10.5 bo string "10.5" jest konwertowany na float 10.5
print(int("10")) # konwersja str na int - wynik 10 bo string "10" jest konwertowany na int 10
print(bool(1)) # konwersja int na bool - wynik True bo 1 jest true
print(bool(0)) # konwersja int na bool - wynik False bo 0 jest false
print(bool("")) # konwersja str na bool - wynik False bo pusty string jest false
# print(int("10.5")) # konwersja str na int - wynik blad bo string "10.5" nie jest konwertowany na int 10.5

# indeksowanie? Czym jest?
# order, kolejnosc, pozycja elementu w kolekcji, w Pythonie indeksowanie zaczyna sie od 0

day = "Monday"
print(day[0]) # wypisanie pierwszego znaku stringa day - wynik "M"
print(day[1]) # wypisanie drugiego znaku stringa day - wynik "o"
print(day[-4]) # wypisanie ostatniego znaku stringa day - wynik "d" bo indeksowanie od tylu zaczyna sie od -1
print(day[-1]) # wypisanie ostatniego znaku stringa day - wynik "y" bo indeksowanie od tylu zaczyna sie od -1
# print(day[6]) # wypisanie siódmego znaku stringa day - wynik blad bo indeksowanie zaczyna sie od 0 i konczy na 5

# slicing - wycinanie fragmentu stringa, w Pythonie slicing jest wykonywany za pomoca operatora [:] - plasterkowanie
print(day[0:3]) # wypisanie pierwszych trzech znakow stringa day - wynik "Mon", bo indeksowanie zaczyna sie od 0 i konczy na 2, 3 nie jest brane pod uwage - zbior jednostrownnie domkniety zawsze wybiera bez ostatniego indeksu
print(day[3:]) # wypisanie znakow stringa day od trzeciego znaku do konca - wynik "day"
print(day[:3]) # wypisanie znakow stringa day od poczatku do trzeciego znaku - wynik "Mon"
print(day[:]) # wypisanie wszystkich znakow stringa day - wynik "Monday"
print(day[1:5:2]) # [start:stop:step] - wypisanie znakow stringa day od pierwszego znaku do piatego znaku co drugi znak - wynik "od" bo indeksowanie zaczyna sie od 0 i konczy na 4, 5 nie jest brane pod uwage, co drugi znak to 1,3

# Metody stringow - sa to funkcje ktore mozna wywolac na stringu, w Pythonie sa to np. upper(), lower(), strip(), replace(), split(), join()
name = "Karolina"   
print(name.upper()) # wypisanie stringa day w duzych literach - wynik "MONDAY"
print(name.lower()) # wypisanie stringa day w malych literach - wynik "monday"
print(name.count("a")) # wypisanie ilosci znakow stringa day 
print(name.startswith("K")) # sprawdzenie czy string name zaczyna sie od litery "K" - wynik True
print(name.endswith("a")) # sprawdzenie czy string name konczy sie na litere "a" - wynik True
print(name.find("o")) # wypisanie indeksu pierwszego wystapienia litery "o" w stringu name - wynik 2
print(name.islower()) # sprawdzenie czy string name jest napisany malymi literami - wynik False
print(name.isupper()) # sprawdzenie czy string name jest napisany duzymi literami - wynik False

print("############")
print(name.replace("a", "o"))#  zamiana wszystkich liter "a" na "o" w stringu name - wynik "Korolino"
print(name)
print((name.lower().capitalize())) # wypisanie stringa name w malych literach z pierwsza litera duza - wynik "Karolina"
print(name)

name = name.replace("a", "o") # przypisanie do zmiennej name stringa name po zamianie wszystkich liter "a" na "o" - wynik "Korolino" - tworzy nam to nowy string i przypisuje go do zmiennej name, bo stringi sa niemutowalne - nowe miejsce w pamieci zostaje zajete na nowy string, a stary string zostaje usuniety z pamieci
print(name) # wypisanie stringa name po zamianie wszystkich liter "a" na "o" - wynik "Korolino"
print(name.replace("o", "a").lower().endswith('a')) # sprawdzenie czy string name po zamianie wszystkich liter "o" na "a" i zamianie na male litery konczy sie na litere "a" - wynik True
print(name.replace("o", "a").upper().endswith('a')) # sprawdzenie czy string name po zamianie wszystkich liter "o" na "a" i zamianie na duzelitery konczy sie na litere "a" - wynik false bo zamiana na duze litery zmienia koncowke na "A" a nie "a"



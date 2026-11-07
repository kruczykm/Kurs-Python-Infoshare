# komentarz - ta czesc nie jest czytana przez interpreter
# skrot - ctrl/cmd + /

#plik .py poprawnie nazywa sie modułem 

#zmienna - pozwala nam przechowywac wartosc pod okreslona nazwa
#operator  = przypisuje wartosc do zmiennej znajdujaca sie po prawej stronie
#do zmiennej po lewej

age = 35 #przypsanie do zmiennej age wartosci 35 (int)
print(age)
print(id(age))

name = 'Karolina' #zmienna przechowuje str
print(name)
print(age, name) 

#nazwy zmiennych
#nie mozna miec spacji
# any variable = 10 #SyntaxError: invalid syntax - niezgodne ze skladnia pythona

#snake case
any_variable = 10 
print(any_variable)

#unikamy nazywania zmiennych tak jak elementy skladowe jezyka
# int = 60 #przypisanie do zmiennej, ktora jest czescia skladni
# print(int)

# int('10') #konwersja typow

New_var = 50 #NewVar
print(New_var)

#M, X - wyjatki, ze mozna z wielkiej litery

# 3m = 10 

#dynamicznie typowany - probuje zrobic z tego cyfre 
# w jezyku c int 5; python 5 (sam nadaje typ)

x = 5

#DUZO LINIJEK KODU
x = 11

#PODSTAWOWE TYPY DANYCH
#INT - całkowita
#STR - text
#FLOAT - zmiennoprzecinkowa
#BOOLEAN - True/False
#NoneType - typ nic xD

#INT - całkowite
#Czy istnieje najwiekszy int?
f = 84526562465528584265452464868246286564
print(f)

print(1+1)
print(1-5)
print(1*4)
print(4/4)
print(4//4) #dzielenie calkowite
print(4**2)
print(14 % 2) #modulo, reszta z dzielenia

number_1 = 10
number_2 = 15
print(number_1 - number_2)

##FLOAT 
#zmiennoprzecinkowa
g = 0.35653676576535366565656536756753763567
print(g)
#float precision

#== sprawdza czy jedna strona jest rowna drugiej
print(0.35653676576535366565656536756753763567 == 0.35653676576535366565656536756753763561)

print(0.1+0.1+0.1)

#STR - napis. Wszystko co jest w str nie jest interpretowane

#""
#''
"It's me"
#"fffff'

#multiline string - w dokumentacji nazywa sie docstring
n = """
Lubie
kotki
w 
wielu
linijkach

"""
print(n)
name = 'Karolina'
last_name = 'Wadowska'
print(name + ' ' + last_name) #konkatenacja, czyli laczenie stringow

print('Python'*3)

##Bool - wartosci logiczne
#Przyjmuje dwie wartosci - True/False, z wielkiej litery

is_student = True
is_admin = False

print(type(is_student))

##booleany sluza jako wynik porownania

print(age > 18)

#> to jest operator porownania

print(5 >= 5)

#nie rowne 
print(5 != 5 )

##None - brak wartosci

result = None
print(type(result))

### zmiana typu - konwersji typow 
# nazwa_typu_docelowego(zmienna do konwersji)
print(int(10.0))

# Male cwiczenie:
# sprobowac przekonwertac np. 5 roznych kombinacji typow
#do 18:10

# print(int('cos'))

print(int(7.99)) #uciecie koncowki, a nie zaokraglenie

print(int(1 + 0.99))

print(round(7.678, 2))

#indeksowanie 
#czym jest indeks? 
#order, kolejnosc
day = 'Saturday'
print(len(day)) #dlugosc stringa - 8 elementow
#PYTHON INDEKSUJE OD 0 
print(day[0]) #wybrane elementu o indeksie 0 
print(day[-1]) #wybranie elementu ostatniego

#Slicing - plasterkowanie
print(day[1:3]) #wybranie od [,) - zbior jednostronniw domkniety
print(day[1:5:2])#[start, stop, step]
print(day[:2]) #od 0 do 2 co 1 - arg domyslne 

#Metody - funkcje, ktora sa przeznaczone ale konkretnych typow danych

#typ_danych.metoda(arument, ale nie musi go byc)
print(name.upper())
print(name.count('a'))

#Zad 2. Przetestuj 2 metody dla stringow, inne niz do tej pory
#czas do 18:30

print(name.replace('a', 'i'))

name = name.replace('a', 'i')
print(name)

print(name.replace('i', 'a').endswith('a').upper())

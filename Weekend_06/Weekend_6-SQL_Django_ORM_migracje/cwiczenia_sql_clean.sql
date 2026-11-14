FILE: cwiczenia_sql_clean.sql

/*
Weekend 6 — SQL + Django ORM + migracje
Plik: cwiczenia_sql_clean.sql

Wersja CLEAN — zadania bez rozwiązań.

Cel pliku:
- przećwiczyć SELECT, WHERE, ORDER BY, LIMIT,
- przećwiczyć JOIN, LEFT JOIN, GROUP BY, HAVING,
- nauczyć się patrzeć na dane jak backend developer,
- przygotować intuicję pod Django ORM i modele Django.

Założenie:
- pracujemy na bazie SQLite albo PostgreSQL przygotowanej z datasetu Olist,
- nazwy tabel są uproszczone:
  - customers
  - orders
  - order_items
  - products
  - sellers
  - order_payments
  - order_reviews

Jeśli pracujesz w SQLite, możesz uruchamiać zapytania np. w DB Browser for SQLite, DBeaver albo przez notebook.
Jeśli pracujesz w PostgreSQL, część funkcji dat może wymagać drobnej zmiany składni.
*/

/*
================================================================================
OPIS DATASETU
================================================================================

Nazwa:
Olist Brazilian E-Commerce Public Dataset

Źródło:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Kontekst biznesowy:
Dataset opisuje brazylijski marketplace e-commerce. Zawiera dane o klientach,
zamówieniach, produktach, sprzedawcach, płatnościach, opiniach i pozycjach
zamówień. To dobry dataset do nauki backendu, ponieważ ma realne relacje
między tabelami i pozwala ćwiczyć typowe raporty oraz zapytania używane
w aplikacjach webowych.

--------------------------------------------------------------------------------
Tabela: customers
--------------------------------------------------------------------------------
customer_id                 TEXT      identyfikator klienta w kontekście zamówienia
customer_unique_id          TEXT      unikalny identyfikator klienta
customer_zip_code_prefix    INTEGER   prefiks kodu pocztowego
customer_city               TEXT      miasto klienta
customer_state              TEXT      stan/region klienta

--------------------------------------------------------------------------------
Tabela: orders
--------------------------------------------------------------------------------
order_id                         TEXT      identyfikator zamówienia
customer_id                      TEXT      klient przypisany do zamówienia
order_status                     TEXT      status zamówienia
order_purchase_timestamp         DATETIME  data złożenia zamówienia
order_approved_at                DATETIME  data akceptacji płatności
order_delivered_carrier_date     DATETIME  data przekazania przewoźnikowi
order_delivered_customer_date    DATETIME  data dostawy do klienta
order_estimated_delivery_date    DATETIME  planowana data dostawy

--------------------------------------------------------------------------------
Tabela: order_items
--------------------------------------------------------------------------------
order_id              TEXT      zamówienie
order_item_id         INTEGER   numer pozycji w zamówieniu
product_id            TEXT      produkt
seller_id             TEXT      sprzedawca
shipping_limit_date   DATETIME  graniczna data wysyłki
price                 DECIMAL   cena produktu
freight_value         DECIMAL   koszt dostawy

--------------------------------------------------------------------------------
Tabela: products
--------------------------------------------------------------------------------
product_id                    TEXT      identyfikator produktu
product_category_name         TEXT      kategoria produktu
product_name_lenght           INTEGER   długość nazwy produktu
product_description_lenght    INTEGER   długość opisu produktu
product_photos_qty            INTEGER   liczba zdjęć produktu
product_weight_g              INTEGER   waga produktu w gramach
product_length_cm             INTEGER   długość produktu
product_height_cm             INTEGER   wysokość produktu
product_width_cm              INTEGER   szerokość produktu

Uwaga: w oryginalnym datasecie występuje literówka "lenght" zamiast "length".
W ćwiczeniach trzymamy się oryginalnych nazw kolumn.

--------------------------------------------------------------------------------
Tabela: sellers
--------------------------------------------------------------------------------
seller_id                 TEXT      identyfikator sprzedawcy
seller_zip_code_prefix    INTEGER   prefiks kodu pocztowego
seller_city               TEXT      miasto sprzedawcy
seller_state              TEXT      stan/region sprzedawcy

--------------------------------------------------------------------------------
Tabela: order_payments
--------------------------------------------------------------------------------
order_id                TEXT      zamówienie
payment_sequential      INTEGER   numer płatności
payment_type            TEXT      typ płatności
payment_installments    INTEGER   liczba rat
payment_value           DECIMAL   wartość płatności

--------------------------------------------------------------------------------
Tabela: order_reviews
--------------------------------------------------------------------------------
review_id                  TEXT      identyfikator opinii
order_id                   TEXT      zamówienie
review_score               INTEGER   ocena 1-5
review_comment_title       TEXT      tytuł opinii
review_comment_message     TEXT      treść opinii
review_creation_date       DATETIME  data wystawienia opinii
review_answer_timestamp    DATETIME  data odpowiedzi

--------------------------------------------------------------------------------
Kategorie i etykiety:
--------------------------------------------------------------------------------
order_status:
- delivered
- shipped
- canceled
- invoiced
- processing
- unavailable
- approved
- created

payment_type:
- credit_card
- boleto
- voucher
- debit_card
- not_defined

review_score:
- liczby od 1 do 5

product_category_name:
- kategorie produktów, np. bed_bath_table, health_beauty, sports_leisure itd.
*/

/*
================================================================================
SEKCJA 0 — SPRAWDZENIE BAZY
================================================================================
*/

/*
Zadanie 0.1 — Lista tabel

Biznes:
Zanim zaczniemy pisać raporty, chcemy sprawdzić, jakie tabele są dostępne.

Cel techniczny:
Sprawdzenie struktury bazy.

Trudność: 1/5
Czas: 5 min

Wskazówki:
- W SQLite użyj sqlite_master.
- W PostgreSQL możesz użyć information_schema.tables.
- Uruchom tylko wariant pasujący do Twojej bazy.
*/

-- TODO SQLite: pokaż listę tabel w bazie.
-- SELECT ...


-- TODO PostgreSQL: pokaż listę tabel publicznych.
-- SELECT ...


/*
Zadanie 0.2 — Podgląd pierwszych rekordów

Biznes:
Chcemy szybko zobaczyć, jak wyglądają dane w każdej głównej tabeli.

Cel techniczny:
SELECT + LIMIT.

Trudność: 1/5
Czas: 8 min

Wskazówki:
- Uruchamiaj zapytania pojedynczo.
- Nie analizuj jeszcze wszystkiego naraz.
- Zwróć uwagę na nazwy identyfikatorów.
*/

-- TODO: podejrzyj 5 rekordów z customers.
-- SELECT ...


-- TODO: podejrzyj 5 rekordów z orders.
-- SELECT ...


-- TODO: podejrzyj 5 rekordów z order_items.
-- SELECT ...


-- TODO: podejrzyj 5 rekordów z products.
-- SELECT ...


-- TODO: podejrzyj 5 rekordów z order_payments.
-- SELECT ...


-- TODO: podejrzyj 5 rekordów z order_reviews.
-- SELECT ...


/*
================================================================================
SEKCJA 1 — SELECT, WHERE, ORDER BY, LIMIT
================================================================================
*/

/*
Zadanie 1 — Pierwszy SELECT z tabeli orders

Biznes:
Support chce podejrzeć próbkę zamówień.

Cel techniczny:
SELECT, FROM, LIMIT.

Trudność: 1/5
Czas: 8 min

Polecenie:
Wybierz 10 rekordów z tabeli orders.
Zwróć kolumny:
- order_id
- customer_id
- order_status
- order_purchase_timestamp

Wskazówki:
- Nie używaj SELECT *.
- Ogranicz wynik przez LIMIT.
- Sprawdź, czy wynik jest czytelny.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 2 — Filtrowanie zamówień po statusie

Biznes:
Dział operacyjny chce analizować tylko zamówienia dostarczone.

Cel techniczny:
WHERE.

Trudność: 1/5
Czas: 8 min

Polecenie:
Pobierz zamówienia, dla których order_status = 'delivered'.
Zwróć:
- order_id
- customer_id
- order_status

Wskazówki:
- Warunek wpisz po WHERE.
- Ogranicz wynik do 20 rekordów.
- Sprawdź, czy w wyniku są tylko zamówienia dostarczone.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 3 — Sortowanie najnowszych zamówień

Biznes:
Panel admina ma pokazywać ostatnie zakupy.

Cel techniczny:
ORDER BY, DESC, LIMIT.

Trudność: 1/5
Czas: 8 min

Polecenie:
Pobierz 15 najnowszych zamówień według order_purchase_timestamp.
Zwróć:
- order_id
- customer_id
- order_status
- order_purchase_timestamp

Wskazówki:
- Sortowanie malejące to DESC.
- Najnowsze rekordy powinny być na górze.
- Zwróć datę, żeby zweryfikować sortowanie.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 4 — Zamówienia z konkretnego okresu

Biznes:
Zespół sprzedaży analizuje sprzedaż w styczniu 2018.

Cel techniczny:
Filtrowanie po datach.

Trudność: 2/5
Czas: 10 min

Polecenie:
Pobierz zamówienia złożone w styczniu 2018 roku.
Zwróć:
- order_id
- order_status
- order_purchase_timestamp

Wskazówki:
- Użyj zakresu od '2018-01-01' do przed '2018-02-01'.
- Przy datach z godziną to często bezpieczniejsze niż BETWEEN.
- Posortuj wynik rosnąco po dacie zakupu.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 5 — Klienci z wybranego stanu

Biznes:
Marketing planuje kampanię regionalną dla stanu SP.

Cel techniczny:
Filtrowanie tekstu i sortowanie.

Trudność: 1/5
Czas: 8 min

Polecenie:
Pobierz klientów ze stanu SP.
Zwróć:
- customer_id
- customer_city
- customer_state

Wskazówki:
- Użyj tabeli customers.
- Warunek dotyczy customer_state.
- Posortuj po customer_city.
- Ogranicz wynik do 30 rekordów.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 6 — Zamówienia anulowane albo niedostępne

Biznes:
Zespół obsługi chce sprawdzić problematyczne zamówienia.

Cel techniczny:
WHERE, IN, ORDER BY.

Trudność: 2/5
Czas: 10 min

Polecenie:
Pobierz zamówienia, których status to canceled albo unavailable.
Zwróć:
- order_id
- customer_id
- order_status
- order_purchase_timestamp

Wskazówki:
- Użyj IN.
- Posortuj od najnowszych.
- Ogranicz wynik do 30 rekordów.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 7 — Produkty bez kategorii

Biznes:
Zespół katalogu chce znaleźć produkty z brakującą kategorią.

Cel techniczny:
IS NULL.

Trudność: 2/5
Czas: 8 min

Polecenie:
Znajdź produkty, dla których product_category_name jest puste/null.
Zwróć:
- product_id
- product_category_name
- product_photos_qty

Wskazówki:
- Użyj IS NULL.
- Ogranicz wynik do 30 rekordów.
- Zastanów się, czy pusty tekst i NULL to zawsze to samo.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
================================================================================
SEKCJA 2 — JOIN
================================================================================
*/

/*
Zadanie 8 — JOIN orders z customers

Biznes:
Support chce widzieć zamówienie razem z lokalizacją klienta.

Cel techniczny:
INNER JOIN.

Trudność: 2/5
Czas: 15 min

Polecenie:
Połącz orders z customers po customer_id.
Zwróć:
- order_id
- order_status
- customer_city
- customer_state

Wskazówki:
- Użyj aliasów o i c.
- Warunek połączenia wpisz po ON.
- Ogranicz wynik do 20 rekordów.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 9 — JOIN orders, order_items, products

Biznes:
Analityk chce sprawdzić, jakie kategorie produktów pojawiają się w zamówieniach.

Cel techniczny:
JOIN wielu tabel.

Trudność: 3/5
Czas: 18 min

Polecenie:
Połącz orders, order_items i products.
Zwróć:
- order_id
- order_status
- product_id
- product_category_name
- price

Wskazówki:
- Najpierw połącz orders z order_items.
- Potem dołącz products.
- Jedno zamówienie może mieć wiele pozycji.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 10 — JOIN z płatnościami

Biznes:
Finance chce analizować typy płatności przy zamówieniach.

Cel techniczny:
JOIN orders + order_payments.

Trudność: 2/5
Czas: 12 min

Polecenie:
Połącz zamówienia z płatnościami.
Zwróć:
- order_id
- order_status
- payment_type
- payment_installments
- payment_value

Wskazówki:
- Łącz po order_id.
- Jedno zamówienie może mieć więcej niż jedną płatność.
- Posortuj po payment_value malejąco.
- Ogranicz wynik do 30 rekordów.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 11 — LEFT JOIN dla zamówień bez opinii

Biznes:
Customer success chce znaleźć zamówienia bez recenzji.

Cel techniczny:
LEFT JOIN, IS NULL.

Trudność: 3/5
Czas: 18 min

Polecenie:
Znajdź zamówienia, które nie mają opinii w tabeli order_reviews.
Zwróć:
- order_id
- order_status
- review_id
- review_score

Wskazówki:
- Zacznij od orders.
- Dołącz order_reviews przez LEFT JOIN.
- Szukaj rekordów, gdzie review_id IS NULL.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 12 — Zamówienia z lokalizacją klienta i typem płatności

Biznes:
Zespół growth chce analizować typy płatności według regionu.

Cel techniczny:
JOIN trzech tabel.

Trudność: 3/5
Czas: 18 min

Polecenie:
Połącz orders, customers i order_payments.
Zwróć:
- order_id
- customer_state
- customer_city
- order_status
- payment_type
- payment_value

Wskazówki:
- orders łączy się z customers po customer_id.
- orders łączy się z order_payments po order_id.
- Używaj aliasów.
- Ogranicz wynik do 50 rekordów.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 13 — Produkty i sprzedawcy

Biznes:
Marketplace chce widzieć, którzy sprzedawcy sprzedają jakie kategorie.

Cel techniczny:
JOIN order_items + products + sellers.

Trudność: 3/5
Czas: 18 min

Polecenie:
Połącz order_items, products i sellers.
Zwróć:
- seller_id
- seller_city
- seller_state
- product_id
- product_category_name
- price

Wskazówki:
- order_items łączy się z products po product_id.
- order_items łączy się z sellers po seller_id.
- Ogranicz wynik do 50 rekordów.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 14 — Debugowanie błędnego JOIN-a

Biznes:
Raport pokazuje podejrzanie dużo rekordów albo puste wyniki.

Cel techniczny:
Diagnoza złego warunku JOIN.

Trudność: 3/5
Czas: 15 min

Polecenie:
Wyjaśnij, dlaczego poniższy pomysł jest błędny:
orders.order_id = customers.customer_id

Następnie napisz poprawny JOIN orders + customers.

Wskazówki:
- Porównaj znaczenie biznesowe kolumn.
- Nie łącz kolumn tylko dlatego, że mają podobny typ.
- Poprawna relacja wynika z modelu danych.
*/

-- TODO: wpisz poprawne zapytanie SQL poniżej.



/*
================================================================================
SEKCJA 3 — GROUP BY I AGREGACJE
================================================================================
*/

/*
Zadanie 15 — Liczba zamówień po statusie

Biznes:
Dashboard operacyjny pokazuje rozkład statusów zamówień.

Cel techniczny:
GROUP BY, COUNT.

Trudność: 2/5
Czas: 10 min

Polecenie:
Policz liczbę zamówień dla każdego order_status.

Wskazówki:
- Grupuj po order_status.
- Nadaj alias, np. orders_count.
- Posortuj wynik malejąco po liczbie zamówień.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 16 — Przychód po kategoriach produktów

Biznes:
Dział sprzedaży chce poznać najlepsze kategorie.

Cel techniczny:
SUM, JOIN, GROUP BY.

Trudność: 3/5
Czas: 20 min

Polecenie:
Policz sumę price dla każdej kategorii produktu.
Pomiń rekordy bez kategorii.

Wskazówki:
- Użyj order_items i products.
- Łącz po product_id.
- W tym zadaniu licz tylko price, bez freight_value.
- Posortuj od najwyższego przychodu.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 17 — Średni koszt dostawy po stanie klienta

Biznes:
Logistyka porównuje regiony pod kątem kosztu dostawy.

Cel techniczny:
AVG, JOIN wielu tabel.

Trudność: 3/5
Czas: 18 min

Polecenie:
Policz średni freight_value dla każdego customer_state.

Wskazówki:
- Potrzebujesz orders, customers i order_items.
- Grupuj po customer_state.
- Posortuj od najwyższego średniego kosztu dostawy.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 18 — Najlepsi sprzedawcy według przychodu

Biznes:
Marketplace chce znaleźć top sellerów.

Cel techniczny:
Agregacja po seller_id.

Trudność: 3/5
Czas: 15 min

Polecenie:
Policz sumę price dla każdego sprzedawcy i pokaż top 10.

Wskazówki:
- Użyj order_items.
- Grupuj po seller_id.
- Dodaj COUNT(*) jako liczbę sprzedanych pozycji.
- Użyj LIMIT 10.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 19 — Kategorie ze średnią oceną poniżej 3

Biznes:
Zespół jakości chce znaleźć problematyczne kategorie produktów.

Cel techniczny:
JOIN, AVG, HAVING.

Trudność: 4/5
Czas: 25 min

Polecenie:
Znajdź kategorie produktów, których średnia ocena review_score jest mniejsza niż 3.

Wskazówki:
- Potrzebujesz products, order_items, orders, order_reviews.
- Droga relacji: products -> order_items -> orders -> order_reviews.
- WHERE filtruje rekordy przed grupowaniem.
- HAVING filtruje grupy po agregacji.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 20 — Raport miesięczny sprzedaży

Biznes:
Zarząd potrzebuje miesięcznego raportu sprzedaży.

Cel techniczny:
Grupowanie po miesiącu.

Trudność: 4/5
Czas: 25 min

Polecenie:
Przygotuj raport miesięczny zawierający:
- miesiąc zakupu,
- liczbę unikalnych zamówień,
- liczbę pozycji zamówień,
- sumę wartości pozycji zamówień.

Wskazówki dla SQLite:
- Użyj strftime('%Y-%m', order_purchase_timestamp).

Wskazówki dla PostgreSQL:
- Użyj DATE_TRUNC('month', order_purchase_timestamp::timestamp).

Uwaga:
Po dołączeniu order_items jedna linia oznacza pozycję zamówienia, nie całe zamówienie.
Do liczby zamówień użyj COUNT(DISTINCT ...).
*/

-- TODO SQLite: wpisz zapytanie SQL poniżej.



-- TODO PostgreSQL: wpisz wariant PostgreSQL poniżej, jeśli pracujesz na PostgreSQL.



/*
Zadanie 21 — Średnia wartość płatności po typie płatności

Biznes:
Finance chce sprawdzić, które typy płatności mają najwyższą średnią wartość.

Cel techniczny:
AVG, GROUP BY, ORDER BY.

Trudność: 2/5
Czas: 12 min

Polecenie:
Dla każdego payment_type policz:
- liczbę płatności,
- średnią payment_value,
- maksymalną payment_value.

Wskazówki:
- Użyj order_payments.
- Grupuj po payment_type.
- Posortuj po średniej wartości malejąco.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 22 — Udział statusów zamówień

Biznes:
Zespół operacyjny chce widzieć, jaki procent zamówień jest dostarczony,
anulowany itd.

Cel techniczny:
COUNT, podzapytanie albo window function.

Trudność: 4/5
Czas: 25 min

Polecenie:
Policz liczbę zamówień per order_status oraz udział procentowy w całości.

Wskazówki:
- Najpierw policz same liczby per status.
- Potem podziel przez całkowitą liczbę zamówień.
- W SQLite możesz użyć podzapytania.
- Pamiętaj o mnożeniu przez 100.0, żeby uniknąć dzielenia całkowitego.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 23 — Sprzedawcy z więcej niż 100 sprzedanymi pozycjami

Biznes:
Marketplace chce znaleźć aktywnych sprzedawców o dużej liczbie sprzedaży.

Cel techniczny:
GROUP BY, COUNT, HAVING.

Trudność: 3/5
Czas: 15 min

Polecenie:
Znajdź sprzedawców, którzy mają więcej niż 100 pozycji w order_items.
Zwróć:
- seller_id
- liczbę pozycji
- sumę price

Wskazówki:
- Użyj HAVING, nie WHERE.
- Posortuj po liczbie pozycji malejąco.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 24 — Kategorie z minimum 100 opiniami

Biznes:
Zespół jakości chce analizować tylko kategorie z sensowną liczbą opinii.

Cel techniczny:
JOIN, GROUP BY, HAVING z COUNT.

Trudność: 4/5
Czas: 25 min

Polecenie:
Dla kategorii produktów policz:
- liczbę opinii,
- średnią ocenę.

Pokaż tylko kategorie z minimum 100 opiniami.

Wskazówki:
- Połącz products, order_items, orders, order_reviews.
- Pomiń puste kategorie.
- Użyj HAVING COUNT(*) >= 100.
- Posortuj po średniej ocenie rosnąco albo malejąco.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
================================================================================
SEKCJA 4 — ANALIZA JAKOŚCI DANYCH
================================================================================
*/

/*
Zadanie 25 — Zamówienia bez daty dostawy

Biznes:
Operacje chcą znaleźć zamówienia, które nie mają daty dostawy do klienta.

Cel techniczny:
IS NULL, filtrowanie statusów.

Trudność: 2/5
Czas: 12 min

Polecenie:
Znajdź zamówienia, gdzie order_delivered_customer_date jest NULL.
Zwróć:
- order_id
- order_status
- order_purchase_timestamp
- order_delivered_customer_date

Wskazówki:
- Użyj IS NULL.
- Posortuj od najnowszych.
- Zastanów się, czy wszystkie takie zamówienia są błędem.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 26 — Dostawy po terminie

Biznes:
Logistyka chce znaleźć zamówienia dostarczone po planowanej dacie.

Cel techniczny:
Porównywanie dat.

Trudność: 3/5
Czas: 18 min

Polecenie:
Znajdź zamówienia, gdzie order_delivered_customer_date jest późniejsza niż
order_estimated_delivery_date.

Zwróć:
- order_id
- order_status
- order_delivered_customer_date
- order_estimated_delivery_date

Wskazówki:
- Odfiltruj rekordy, gdzie data dostawy jest NULL.
- Porównaj dwie kolumny dat.
- Ogranicz wynik do 50 rekordów.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 27 — Produkty z brakującymi wymiarami

Biznes:
Katalog produktów wymaga uzupełnienia danych logistycznych.

Cel techniczny:
IS NULL, OR.

Trudność: 2/5
Czas: 12 min

Polecenie:
Znajdź produkty, które mają brakującą wagę, długość, wysokość albo szerokość.

Zwróć:
- product_id
- product_category_name
- product_weight_g
- product_length_cm
- product_height_cm
- product_width_cm

Wskazówki:
- Użyj warunków OR.
- Ogranicz wynik do 50 rekordów.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 28 — Płatności o wartości zero lub ujemnej

Biznes:
Finance chce sprawdzić potencjalnie błędne płatności.

Cel techniczny:
Filtrowanie wartości liczbowych.

Trudność: 2/5
Czas: 10 min

Polecenie:
Znajdź płatności, gdzie payment_value <= 0.

Wskazówki:
- Użyj order_payments.
- Zwróć order_id, payment_type, payment_value.
- Sprawdź, czy istnieją takie rekordy.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
================================================================================
SEKCJA 5 — PODZAPYTANIA I CTE
================================================================================
*/

/*
Zadanie 29 — Zamówienia droższe niż średnia

Biznes:
Sprzedaż chce znaleźć zamówienia o ponadprzeciętnej wartości pozycji.

Cel techniczny:
CTE albo podzapytanie.

Trudność: 4/5
Czas: 30 min

Polecenie:
Najpierw policz wartość każdego zamówienia jako SUM(order_items.price).
Następnie pokaż tylko zamówienia, których wartość jest większa niż średnia
wartość zamówienia.

Wskazówki:
- Przyda się CTE, np. order_totals.
- Najpierw napisz zapytanie liczące wartość per order_id.
- Potem policz średnią z tych wartości.
- Na końcu odfiltruj zamówienia powyżej średniej.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 30 — Top kategoria w każdym stanie klienta

Biznes:
Growth chce wiedzieć, jakie kategorie są najważniejsze w poszczególnych regionach.

Cel techniczny:
Agregacja, CTE, opcjonalnie funkcja okna.

Trudność: 5/5
Czas: 40 min

Polecenie:
Dla każdego customer_state znajdź kategorię produktu z największą sumą price.

Wskazówki:
- Połącz customers, orders, order_items, products.
- Policz total_revenue per customer_state i product_category_name.
- W PostgreSQL możesz użyć ROW_NUMBER() OVER (...).
- W SQLite też możesz użyć window functions w nowszych wersjach.
- Jeśli to za trudne, najpierw pokaż ranking kategorii per stan bez wybierania top 1.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 31 — Klienci z więcej niż jednym zamówieniem

Biznes:
Marketing chce znaleźć klientów powracających.

Cel techniczny:
GROUP BY, HAVING.

Trudność: 3/5
Czas: 18 min

Polecenie:
Znajdź customer_unique_id, którzy mają więcej niż jedno zamówienie.

Wskazówki:
- orders ma customer_id.
- customers ma customer_unique_id.
- Połącz orders z customers.
- Grupuj po customer_unique_id.
- Użyj HAVING COUNT(DISTINCT order_id) > 1.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 32 — Średni czas od zakupu do akceptacji płatności

Biznes:
Finance chce sprawdzić, jak szybko zamówienia są akceptowane.

Cel techniczny:
Operacje na datach.

Trudność: 4/5
Czas: 30 min

Polecenie:
Policz średni czas między order_purchase_timestamp a order_approved_at.

Wskazówki SQLite:
- Możesz użyć julianday(order_approved_at) - julianday(order_purchase_timestamp).
- Wynik w dniach pomnóż przez 24, jeśli chcesz godziny.

Wskazówki PostgreSQL:
- Możesz odjąć timestampy i użyć EXTRACT(EPOCH FROM ...).

Uwaga:
- Odfiltruj rekordy, gdzie order_approved_at jest NULL.
*/

-- TODO SQLite: wpisz zapytanie SQL poniżej.



-- TODO PostgreSQL: wpisz wariant PostgreSQL poniżej, jeśli pracujesz na PostgreSQL.



/*
================================================================================
SEKCJA 6 — MAPOWANIE SQL NA DJANGO ORM
================================================================================

W tej sekcji nie piszemy kodu Pythona, ale opisujemy, jak dane zapytanie
mogłoby zostać później przeniesione do Django ORM.

Dla każdego zadania:
1. Napisz SQL.
2. W komentarzu opisz, jakie modele Django byłyby potrzebne.
3. W komentarzu opisz, jakie relacje wykorzystałby ORM.
*/

/*
Zadanie 33 — SQL pod endpoint listy zamówień

Biznes:
Endpoint API ma zwracać listę zamówień razem z emailem klienta i statusem.

Cel techniczny:
JOIN i myślenie pod przyszłe API.

Trudność: 3/5
Czas: 20 min

Polecenie:
Napisz SQL pobierający:
- order_id
- order_status
- order_purchase_timestamp
- customer_unique_id
- customer_city
- customer_state

Wskazówki:
- Połącz orders z customers.
- Posortuj po dacie zakupu malejąco.
- Ogranicz do 50 rekordów.

Dodatkowo w komentarzu napisz:
- jakie modele Django byłyby potrzebne,
- gdzie byłby ForeignKey,
- czy w ORM przydałby się select_related.
*/

-- TODO: wpisz zapytanie SQL poniżej.


-- TODO komentarz ORM:
-- Modele:
-- Relacja:
-- Potencjalna optymalizacja:


/*
Zadanie 34 — SQL pod endpoint szczegółów zamówienia

Biznes:
Endpoint szczegółów zamówienia ma pokazywać pozycje zamówienia i produkty.

Cel techniczny:
JOIN orders + order_items + products.

Trudność: 3/5
Czas: 20 min

Polecenie:
Dla wybranego order_id pobierz:
- order_id
- order_status
- order_item_id
- product_id
- product_category_name
- price
- freight_value

Wskazówki:
- Wstaw przykładowy order_id po sprawdzeniu danych.
- Najpierw pobierz dowolny order_id z order_items.
- Potem użyj go w WHERE.
*/

-- TODO: najpierw znajdź przykładowe order_id.
-- SELECT ...


-- TODO: wpisz właściwe zapytanie SQL poniżej.


-- TODO komentarz ORM:
-- Modele:
-- Relacje:
-- Czy użyć prefetch_related? Dlaczego?


/*
Zadanie 35 — SQL pod raport w panelu admina

Biznes:
Admin chce widzieć liczbę zamówień i przychód per status.

Cel techniczny:
JOIN, GROUP BY, COUNT DISTINCT, SUM.

Trudność: 4/5
Czas: 25 min

Polecenie:
Dla każdego order_status policz:
- liczbę unikalnych zamówień,
- liczbę pozycji zamówień,
- sumę price.

Wskazówki:
- Połącz orders z order_items.
- COUNT(DISTINCT order_id) przyda się do liczby zamówień.
- COUNT(*) będzie liczył pozycje zamówień.
*/

-- TODO: wpisz zapytanie SQL poniżej.


-- TODO komentarz ORM:
-- Jak wyglądałoby values(...).annotate(...)?
-- Jakie agregacje byłyby potrzebne?


/*
================================================================================
SEKCJA 7 — PROJEKTOWANIE SCHEMATU POD DJANGO
================================================================================
*/

/*
Zadanie 36 — Minimalny schemat SQL dla modułu orders

Biznes:
Projektujesz własny moduł zamówień w aplikacji Django.

Cel techniczny:
CREATE TABLE, PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE.

Trudność: 4/5
Czas: 35 min

Polecenie:
Zaprojektuj uproszczone tabele:
- app_customers
- app_products
- app_orders
- app_order_items

Wymagania:
- customer ma email unikalny,
- order ma FK do customer,
- order_item ma FK do order i product,
- quantity musi być większe od 0,
- unit_price nie może być ujemne,
- jeden product może pojawić się tylko raz w jednym order.

Wskazówki:
- To nie musi być identyczny SQL jak wygenerowany przez Django.
- Chodzi o zrozumienie, co Django models i migracje robią pod spodem.
- Możesz użyć INTEGER PRIMARY KEY dla SQLite.
*/

-- TODO: zaprojektuj CREATE TABLE app_customers.



-- TODO: zaprojektuj CREATE TABLE app_products.



-- TODO: zaprojektuj CREATE TABLE app_orders.



-- TODO: zaprojektuj CREATE TABLE app_order_items.



/*
Zadanie 37 — Test constraints

Biznes:
Chcemy sprawdzić, czy baza pilnuje reguł jakości danych.

Cel techniczny:
INSERT i oczekiwane błędy constraints.

Trudność: 4/5
Czas: 25 min

Polecenie:
Po utworzeniu tabel z zadania 36 przygotuj testowe INSERT-y:
1. poprawny customer,
2. poprawny product,
3. poprawny order,
4. poprawny order_item,
5. błędny order_item z quantity = 0,
6. błędny order_item z unit_price < 0,
7. duplikat produktu w tym samym zamówieniu.

Wskazówki:
- Uruchamiaj INSERT-y pojedynczo.
- Błędne INSERT-y powinny zakończyć się błędem.
- To dobry sposób na zrozumienie CheckConstraint i UniqueConstraint w Django.
*/

-- TODO: INSERT poprawny customer.



-- TODO: INSERT poprawny product.



-- TODO: INSERT poprawny order.



-- TODO: INSERT poprawny order_item.



-- TODO: INSERT błędny order_item z quantity = 0.



-- TODO: INSERT błędny order_item z unit_price < 0.



-- TODO: INSERT duplikatu produktu w tym samym zamówieniu.



/*
================================================================================
SEKCJA 8 — MINI-PROJEKT SQL
================================================================================
*/

/*
Zadanie 38 — Mini-projekt: raport operacyjny marketplace

Biznes:
Pracujesz jako junior backend developer w marketplace.
Masz przygotować zapytanie do raportu operacyjnego dla zespołu biznesowego.

Cel techniczny:
Połączenie SELECT, JOIN, GROUP BY, HAVING, ORDER BY.

Trudność: 5/5
Czas: 45 min

Polecenie:
Przygotuj raport kategorii produktów zawierający:
- product_category_name,
- liczbę unikalnych zamówień,
- liczbę pozycji zamówień,
- sumę price,
- średnią freight_value,
- średnią review_score.

Pokaż tylko kategorie:
- bez NULL w product_category_name,
- z minimum 100 pozycjami zamówień.

Posortuj:
- od najwyższej sumy price.

Wskazówki:
- Potrzebujesz products, order_items, orders, order_reviews.
- Uważaj na zwielokrotnienie rekordów.
- Do liczby zamówień użyj COUNT(DISTINCT ...).
- Do filtrowania grup użyj HAVING.
- Zastanów się, czy brak opinii powinien wykluczać kategorię z raportu.
*/

-- TODO: wpisz zapytanie SQL poniżej.



/*
Zadanie 39 — Mini-projekt: przygotowanie zapytań pod API

Biznes:
Masz przygotować SQL-ową intuicję dla przyszłych endpointów Django REST API.

Cel techniczny:
Projektowanie zapytań pod realne use-case'y backendowe.

Trudność: 4/5
Czas: 40 min

Polecenie:
Napisz po jednym zapytaniu SQL dla każdego endpointu:

1. Lista ostatnich zamówień.
2. Szczegóły jednego zamówienia z pozycjami.
3. Lista zamówień klienta.
4. Ranking kategorii po przychodzie.
5. Lista zamówień bez opinii.

Wskazówki:
- Każde zapytanie powinno mieć jasne WHERE/JOIN.
- W komentarzu dopisz, jakie modele Django i relacje będą potrzebne.
- Myśl o tym, czy w ORM użyjesz select_related czy prefetch_related.
*/

-- TODO 39.1: lista ostatnich zamówień.



-- TODO 39.2: szczegóły jednego zamówienia z pozycjami.



-- TODO 39.3: lista zamówień klienta.



-- TODO 39.4: ranking kategorii po przychodzie.



-- TODO 39.5: lista zamówień bez opinii.



/*
================================================================================
CHECKLISTA PO ZAKOŃCZENIU
================================================================================

Po wykonaniu zadań sprawdź, czy umiesz:

[ ] Napisać SELECT z konkretnymi kolumnami.
[ ] Użyć WHERE do filtrowania tekstu, liczb i dat.
[ ] Użyć ORDER BY i LIMIT.
[ ] Połączyć dwie tabele przez JOIN.
[ ] Połączyć trzy lub więcej tabel.
[ ] Wyjaśnić różnicę między INNER JOIN i LEFT JOIN.
[ ] Rozpoznać, kiedy JOIN zwielokrotnia rekordy.
[ ] Użyć GROUP BY i COUNT.
[ ] Użyć SUM, AVG, MIN, MAX.
[ ] Wyjaśnić różnicę między WHERE i HAVING.
[ ] Użyć COUNT(DISTINCT ...).
[ ] Napisać prosty raport miesięczny.
[ ] Wskazać PK i FK w relacjach.
[ ] Zaprojektować prostą tabelę pośrednią.
[ ] Wyjaśnić, jak SQL mapuje się na Django models.
[ ] Wyjaśnić, kiedy w ORM przyda się select_related.
[ ] Wyjaśnić, kiedy w ORM przyda się prefetch_related.
[ ] Połączyć ten blok z własnym projektem końcowym.
*/
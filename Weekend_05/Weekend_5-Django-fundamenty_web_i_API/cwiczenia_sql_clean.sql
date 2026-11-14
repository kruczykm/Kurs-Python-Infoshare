FILE: cwiczenia_sql_clean.sql

/*
Opis datasetu

Ten blok weekendowy nie ma dedykowanej części SQL. Głównym celem jest zrozumienie fundamentów Django, routingu, widoków, Django REST Framework, serializerów, statusów HTTP oraz testów endpointów.

Poniższy plik jest opcjonalnym dodatkiem dla osób, które chcą zobaczyć, jak dane używane w API mogłyby później wyglądać w relacyjnej bazie danych.

Właściwa praca z bazą, modelami Django, migracjami, PostgreSQL i SQL będzie rozwijana w kolejnych blokach kursu.

Dataset koncepcyjny:
- Nazwa: Task Management API
- Źródło: dane lokalne tworzone podczas ćwiczeń w API Django
- Główna tabela: tasks
- Cel biznesowy: przechowywanie zadań projektowych zespołu

Tabela: tasks

Kolumny:
- id INTEGER PRIMARY KEY
  Unikalny identyfikator zadania.

- title VARCHAR(120) NOT NULL
  Krótka nazwa zadania widoczna na liście.

- description TEXT
  Dłuższy opis zadania.

- status VARCHAR(20) NOT NULL
  Status pracy nad zadaniem.
  Dozwolone wartości koncepcyjne: todo, in_progress, done.

- priority VARCHAR(20) NOT NULL
  Priorytet zadania.
  Dozwolone wartości koncepcyjne: low, medium, high.

- created_at TIMESTAMP
  Data i czas utworzenia zadania.

Uwaga:
Ten plik nie jest wymagany do realizacji weekendu 5. Można go potraktować jako zapowiedź kolejnych bloków o bazach danych i Django ORM.
*/


-- ============================================================
-- Ćwiczenie SQL 1 — Projekt tabeli tasks
-- ============================================================

/*
Opis biznesowy:
Aplikacja do zarządzania zadaniami potrzebuje trwałego miejsca do przechowywania zadań.

Cel techniczny:
Zaprojektuj tabelę `tasks`, która mogłaby przechowywać dane używane teraz w API.

Trudność: 2/5
Szacowany czas: 15 min

Wskazówki:
1. Zacznij od kolumn: id, title, description, status, priority, created_at.
2. Zastanów się, które pola powinny być wymagane.
3. Nie przejmuj się jeszcze relacjami z użytkownikami.
*/

-- TODO: Napisz CREATE TABLE tasks (...)


-- ============================================================
-- Ćwiczenie SQL 2 — Dodanie przykładowych zadań
-- ============================================================

/*
Opis biznesowy:
Zespół projektowy chce mieć kilka przykładowych zadań startowych.

Cel techniczny:
Dodaj 3 rekordy do tabeli `tasks`.

Trudność: 1/5
Szacowany czas: 10 min

Wskazówki:
1. Użyj statusów: todo, in_progress, done.
2. Użyj priorytetów: low, medium, high.
3. Tytuły powinny przypominać zadania z weekendu Django.
*/

-- TODO: Napisz INSERT INTO tasks (...)


-- ============================================================
-- Ćwiczenie SQL 3 — Pobranie wszystkich zadań
-- ============================================================

/*
Opis biznesowy:
Frontend potrzebuje pobrać listę zadań do wyświetlenia w panelu.

Cel techniczny:
Napisz zapytanie pobierające wszystkie zadania.

Trudność: 1/5
Szacowany czas: 5 min

Wskazówki:
1. Użyj SELECT.
2. Na razie możesz pobrać wszystkie kolumny.
3. Pomyśl, jak to odpowiada endpointowi GET /api/tasks/.
*/

-- TODO: Napisz SELECT ...


-- ============================================================
-- Ćwiczenie SQL 4 — Pobranie zadań według statusu
-- ============================================================

/*
Opis biznesowy:
Użytkownik chce zobaczyć tylko zadania, które są jeszcze do zrobienia.

Cel techniczny:
Pobierz zadania ze statusem `todo`.

Trudność: 1/5
Szacowany czas: 5 min

Wskazówki:
1. Użyj WHERE.
2. Status porównuj jako tekst.
3. To później może stać się filtrem w API.
*/

-- TODO: Napisz SELECT z WHERE status = 'todo'


-- ============================================================
-- Ćwiczenie SQL 5 — Pobranie zadań wysokiego priorytetu
-- ============================================================

/*
Opis biznesowy:
Product owner chce szybko zobaczyć najważniejsze zadania.

Cel techniczny:
Pobierz zadania z priorytetem `high`.

Trudność: 1/5
Szacowany czas: 5 min

Wskazówki:
1. Użyj WHERE priority = 'high'.
2. Posortuj wynik po dacie utworzenia, jeśli masz kolumnę created_at.
3. Zastanów się, czy API powinno mieć kiedyś filtr `?priority=high`.
*/

-- TODO: Napisz SELECT ...


-- ============================================================
-- Ćwiczenie SQL 6 — Sortowanie zadań
-- ============================================================

/*
Opis biznesowy:
Lista zadań powinna pokazywać najnowsze zadania na górze.

Cel techniczny:
Pobierz zadania posortowane malejąco po `created_at`.

Trudność: 1/5
Szacowany czas: 5 min

Wskazówki:
1. Użyj ORDER BY.
2. Malejąco oznacza DESC.
3. Jeśli nie masz created_at, posortuj po id malejąco.
*/

-- TODO: Napisz SELECT z ORDER BY ...


-- ============================================================
-- Ćwiczenie SQL 7 — Liczba zadań według statusu
-- ============================================================

/*
Opis biznesowy:
Zespół chce wiedzieć, ile zadań jest do zrobienia, w trakcie i zakończonych.

Cel techniczny:
Policz zadania w każdej kategorii statusu.

Trudność: 2/5
Szacowany czas: 10 min

Wskazówki:
1. Użyj COUNT.
2. Użyj GROUP BY status.
3. Wynik powinien mieć kolumny: status, task_count.
*/

-- TODO: Napisz SELECT status, COUNT(*) ...


-- ============================================================
-- Ćwiczenie SQL 8 — Aktualizacja statusu zadania
-- ============================================================

/*
Opis biznesowy:
Użytkownik zakończył zadanie i chce zmienić jego status na `done`.

Cel techniczny:
Zaktualizuj status wybranego zadania.

Trudność: 2/5
Szacowany czas: 10 min

Wskazówki:
1. Użyj UPDATE.
2. Nie zapomnij o WHERE.
3. Bez WHERE zmienisz wszystkie rekordy.
*/

-- TODO: Napisz UPDATE tasks SET status = 'done' WHERE ...


-- ============================================================
-- Ćwiczenie SQL 9 — Usunięcie zadania
-- ============================================================

/*
Opis biznesowy:
Zadanie zostało utworzone przez pomyłkę i trzeba je usunąć.

Cel techniczny:
Usuń jedno zadanie po identyfikatorze.

Trudność: 2/5
Szacowany czas: 10 min

Wskazówki:
1. Użyj DELETE.
2. Zawsze dodaj WHERE.
3. Przed DELETE możesz wykonać SELECT dla tego id.
*/

-- TODO: Napisz DELETE FROM tasks WHERE ...


-- ============================================================
-- Ćwiczenie SQL 10 — Walidacja koncepcyjna statusu
-- ============================================================

/*
Opis biznesowy:
Backend nie powinien przyjmować statusu spoza procesu pracy zespołu.

Cel techniczny:
Zastanów się, jak w SQL można ograniczyć wartości pola `status`.

Trudność: 3/5
Szacowany czas: 15 min

Wskazówki:
1. Możesz użyć CHECK constraint.
2. Dozwolone wartości to: todo, in_progress, done.
3. Porównaj to z ChoiceField w serializerze DRF.
*/

-- TODO: Zaproponuj CHECK constraint dla kolumny status


-- ============================================================
-- Ćwiczenie SQL 11 — Walidacja koncepcyjna priorytetu
-- ============================================================

/*
Opis biznesowy:
Priorytet powinien mieć tylko wartości obsługiwane przez aplikację.

Cel techniczny:
Zastanów się, jak ograniczyć wartości pola `priority`.

Trudność: 3/5
Szacowany czas: 10 min

Wskazówki:
1. Dozwolone wartości to: low, medium, high.
2. Możesz użyć CHECK.
3. Ta sama walidacja powinna później istnieć w API i bazie.
*/

-- TODO: Zaproponuj CHECK constraint dla kolumny priority


-- ============================================================
-- Ćwiczenie SQL 12 — Mapowanie SQL na API
-- ============================================================

/*
Opis biznesowy:
Backend developer musi rozumieć, jak endpoint API przekłada się na operacje na bazie danych.

Cel techniczny:
Dopasuj operacje API do operacji SQL.

Trudność: 2/5
Szacowany czas: 15 min

Uzupełnij koncepcyjnie:

1. GET /api/tasks/
   SQL: ...

2. POST /api/tasks/
   SQL: ...

3. GET /api/tasks/{id}/
   SQL: ...

4. PATCH /api/tasks/{id}/
   SQL: ...

5. DELETE /api/tasks/{id}/
   SQL: ...

Wskazówki:
1. GET zwykle odpowiada SELECT.
2. POST zwykle odpowiada INSERT.
3. PATCH zwykle odpowiada UPDATE.
4. DELETE zwykle odpowiada DELETE.
*/

-- TODO: Zapisz przykładowe zapytania SQL jako komentarze poniżej.


-- ============================================================
-- Ćwiczenie SQL 13 — Przygotowanie pod przyszły Django ORM
-- ============================================================

/*
Opis biznesowy:
W kolejnym etapie tabela SQL zostanie zastąpiona modelem Django.

Cel techniczny:
Zastanów się, jak kolumny SQL mapują się na pola modelu Django.

Trudność: 2/5
Szacowany czas: 15 min

Uzupełnij koncepcyjnie:

SQL:
- VARCHAR(120) -> Django field: ...
- TEXT -> Django field: ...
- TIMESTAMP -> Django field: ...
- INTEGER PRIMARY KEY -> Django field: ...

Wskazówki:
1. CharField wymaga max_length.
2. TextField nadaje się na dłuższy opis.
3. DateTimeField może mieć auto_now_add=True.
4. Django domyślnie tworzy id automatycznie.
*/

-- TODO: Zapisz mapowanie jako komentarz.


-- ============================================================
-- Koniec pliku
-- ============================================================

/*
Ten plik jest dodatkiem koncepcyjnym. Nie jest wymagany do działania weekendu 5.

Najważniejsze w tym bloku pozostaje:
- Django project,
- Django app,
- routing,
- views,
- serializers,
- API endpoints,
- HTTP statuses,
- endpoint tests.

Do SQL, PostgreSQL, migracji i modeli Django wrócimy szerzej w kolejnych blokach.
*/
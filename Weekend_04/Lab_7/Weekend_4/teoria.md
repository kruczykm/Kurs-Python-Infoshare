# 📚 Weekend 4 — teoria: OOP, testy w pytest, jakość kodu i CI

> **Kurs:** AI Python Engineer
> **Temat:** klasy domenowe, testy jednostkowe, Black, Ruff, pre-commit, GitHub Actions
> **Poziom:** 2/5
> **Cel:** przejście od pojedynczych funkcji do klas domenowych zabezpieczonych testami i automatyczną kontrolą jakości.

---

## 🧭 Spis treści

**Sobota — OOP i pytest**
1. [Dlaczego organizujemy kod w klasy?](#1-dlaczego-organizujemy-kod-w-klasy)
2. [Klasa, obiekt i stan](#2-klasa-obiekt-i-stan)
3. [Konstruktor, `self` i atrybuty](#3-konstruktor-self-i-atrybuty)
4. [Walidacja i wyjątki](#4-walidacja-i-wyjątki)
5. [Mutowalny stan i kolekcje](#5-mutowalny-stan-i-kolekcje)
6. [Dziedziczenie i kompozycja](#6-dziedziczenie-i-kompozycja)
7. [Podstawy pytest i AAA](#7-podstawy-pytest-i-aaa)
8. [Testowanie wyjątków](#8-testowanie-wyjątków)
9. [Parametryzacja](#9-parametryzacja)
10. [Fixtures i `conftest.py`](#10-fixtures-i-conftestpy)
11. [Coverage](#11-coverage)

**Niedziela — jakość kodu i CI**
12. [Organizacja testów w większym projekcie](#12-organizacja-testów-w-większym-projekcie)
13. [`pytest.approx` dla liczb zmiennoprzecinkowych](#13-pytestapprox-dla-liczb-zmiennoprzecinkowych)
14. [Testowanie zachowania, nie implementacji](#14-testowanie-zachowania-nie-implementacji)
15. [Black — formatowanie kodu](#15-black--formatowanie-kodu)
16. [Ruff — linting kodu](#16-ruff--linting-kodu)
17. [`pyproject.toml`](#17-pyprojecttoml)
18. [pre-commit](#18-pre-commit)
19. [CI i GitHub Actions](#19-ci-i-github-actions)
20. [Jak czytać błędy z CI?](#20-jak-czytać-błędy-z-ci)
21. [AI jako pomocnik](#21-ai-jako-pomocnik)
22. [Szybka ściąga komend](#22-szybka-ściąga-komend)
23. [Podsumowanie](#23-podsumowanie)

---

# Sobota — OOP i pytest

## 1. Dlaczego organizujemy kod w klasy?

Mały program da się napisać na zmiennych, listach, słownikach i funkcjach:

```python
user = {"email": "anna@example.com", "role": "agent", "is_active": True}

def deactivate_user(user: dict) -> None:
    user["is_active"] = False

def can_manage_documents(user: dict) -> bool:
    return user["is_active"] and user["role"] in {"agent", "admin"}
```

To działa, ale wraz z rozwojem aplikacji backendowej pojawiają się problemy: słownik może nie mieć klucza, nazwa klucza może mieć literówkę, dane i operacje żyją osobno, reguły biznesowe rozjeżdżają się po plikach.

Klasa łączy dane, operacje, walidację i reguły biznesowe w jednej, spójnej strukturze:

```python
class User:
    def __init__(self, email: str, role: str = "user") -> None:
        self.email = email
        self.role = role
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False

    def can_manage_documents(self) -> bool:
        return self.is_active and self.role in {"agent", "admin"}
```

> [!TIP]
> Klasa ma sens wtedy, gdy dane i operacje razem reprezentują konkretne pojęcie biznesowe — w naszym projekcie `ai-knowledge-desk`: `User`, `Document`, `KnowledgeBase`, `SupportTicket`.

## 2. Klasa, obiekt i stan

**Klasa** opisuje rodzaj obiektów — jakie dane przechowują, jakie operacje udostępniają, jakie stany są dozwolone. **Obiekt (instancja)** to konkretny egzemplarz:

```python
first_user = User(email="anna@example.com")
second_user = User(email="jan@example.com")

print(isinstance(first_user, User))   # True
print(first_user is second_user)      # False — dwie różne instancje
```

**Stan** to aktualne dane instancji (`email`, `role`, `is_active`). **Zachowanie** to operacje, które obiekt może wykonać (`deactivate()`, `add_comment()`, `close()`).

## 3. Konstruktor, `self` i atrybuty

`__init__` ustawia stan początkowy obiektu. `self` wskazuje konkretną instancję, na której działa metoda — nie przekazujemy go ręcznie:

```python
user.deactivate()          # tak
User.deactivate(user)      # to dzieje się "pod spodem"
```

Atrybut to wartość powiązana z obiektem (`self.email = email`). W ważnych zmianach biznesowych używamy metody zamiast bezpośredniej zmiany atrybutu — metoda może dodatkowo walidować i pilnować reguł:

```python
user.is_active = False     # omija reguły biznesowe — unikaj
user.deactivate()          # przechodzi przez kontrolowane zachowanie — preferuj
```

**Funkcja a metoda:** funkcja istnieje niezależnie od klasy i otrzymuje dane przez argumenty (`function(user)`); metoda jest zdefiniowana w klasie i korzysta ze stanu przez `self` (`user.method()`).

## 4. Walidacja i wyjątki

Obiekt powinien być poprawny od momentu utworzenia — walidację wykonujemy **przed** przypisaniem atrybutów:

```python
class User:
    ALLOWED_ROLES = {"user", "agent", "admin"}

    def __init__(self, email: str, role: str = "user") -> None:
        if not email.strip():
            raise ValueError("Email cannot be empty")
        if role not in self.ALLOWED_ROLES:
            raise ValueError("Unsupported role")

        self.email = email
        self.role = role
        self.is_active = True
```

`.strip()` odrzuca pusty tekst i tekst złożony wyłącznie ze spacji. Zbiór (`{"user", "agent", "admin"}`) dobrze nadaje się do sprawdzania przynależności (`role in self.ALLOWED_ROLES`).

Wyjątek nie zawsze oznacza awarię — często jest kontrolowaną odpowiedzią na złamanie reguły biznesowej: `ValueError` (niedozwolona wartość), `LookupError` (nie znaleziono obiektu, np. w `KnowledgeBase.get_document`).

## 5. Mutowalny stan i kolekcje

Każda instancja powinna mieć **własną** listę — twórz ją w `__init__`, nie jako atrybut klasy:

```python
# Błędnie — lista współdzielona przez wszystkie instancje
class Document:
    tags = []

# Poprawnie
class Document:
    def __init__(self, document_id: int, title: str, content: str) -> None:
        self.tags: list[str] = []
```

To samo dotyczy argumentów domyślnych — nigdy `tags: list = []`:

```python
def __init__(self, tags: list[str] | None = None) -> None:
    self.tags = [] if tags is None else list(tags)
```

Przykład normalizacji i unikania duplikatów (`Document.add_tag`):

```python
def add_tag(self, tag: str) -> None:
    normalized_tag = tag.strip().lower()
    if not normalized_tag:
        raise ValueError("Tag cannot be empty")
    if normalized_tag not in self.tags:
        self.tags.append(normalized_tag)
```

## 6. Dziedziczenie i kompozycja

**Dziedziczenie** opisuje relację „jest rodzajem”:

```python
class AdminUser(User):
    def __init__(self, email: str) -> None:
        super().__init__(email=email, role="admin")
```

**Kompozycja** opisuje relację „posiada” — `KnowledgeBase` posiada dokumenty, `SupportTicket` posiada autora (`User`):

```python
class KnowledgeBase:
    def __init__(self, name: str) -> None:
        self.documents: list[Document] = []
```

> [!IMPORTANT]
> Nie używaj dziedziczenia tylko po to, żeby nie powtarzać kilku linii kodu — najpierw sprawdź, czy relacja „jest rodzajem” jest biznesowo prawdziwa. W tym bloku dziedziczenie (`AdminUser(User)`) jest świadomie proste — nie budujemy rozbudowanych hierarchii.

## 7. Podstawy pytest i AAA

`pytest` automatycznie wykrywa pliki `test_*.py` i funkcje `test_*`.

```python
def test_user_is_active_after_creation() -> None:
    user = User(email="anna@example.com")

    assert user.is_active is True
```

```bash
pytest              # wszystkie testy
pytest -v           # szczegółowy raport
pytest tests/test_users.py::test_deactivate_changes_user_status   # jeden test
pytest -k deactivate                                              # filtrowanie po nazwie
```

Test dobrze jest dzielić na trzy etapy — **Arrange–Act–Assert (AAA)**:

```python
def test_deactivate_changes_user_status() -> None:
    # Arrange
    user = User(email="anna@example.com")
    # Act
    user.deactivate()
    # Assert
    assert user.is_active is False
```

Komentarze `Arrange`/`Act`/`Assert` są pomocne na początku nauki; później wystarczą czytelna nazwa testu i puste linie rozdzielające etapy.

**Dobra nazwa testu** opisuje testowaną funkcję, warunek i oczekiwany rezultat: `test_close_rejects_already_closed_ticket` — nie `test_1`, `test_it_works`.

## 8. Testowanie wyjątków

```python
import pytest

def test_user_rejects_empty_email() -> None:
    with pytest.raises(ValueError, match="Email cannot be empty"):
        User(email="")
```

Kod, który ma rzucić wyjątek, musi znajdować się **wewnątrz** bloku `with`. Parametr `match` warto stosować, gdy komunikat jest częścią kontraktu funkcji (trafia do API, jest pokazywany użytkownikowi) — nie zawsze jest to konieczne.

## 9. Parametryzacja

```python
@pytest.mark.parametrize(
    ("role", "expected"),
    [("user", False), ("agent", True), ("admin", True)],
)
def test_can_manage_documents_depends_on_role(role: str, expected: bool) -> None:
    user = User(email="person@example.com", role=role)

    assert user.can_manage_documents() is expected
```

Parametryzuj przypadki, które sprawdzają **tę samą regułę** dla różnych danych. Jeśli tabela ma 8 kolumn albo miesza kilka niezależnych zachowań — podziel ją na kilka prostych testów.

## 10. Fixtures i `conftest.py`

Fixture przygotowuje dane lub obiekt potrzebny w teście; pytest wstrzykuje ją po nazwie argumentu:

```python
@pytest.fixture
def regular_user() -> User:
    return User(email="user@example.com")

@pytest.fixture
def support_ticket(regular_user: User) -> SupportTicket:
    return SupportTicket(ticket_id=1, title="Problem z logowaniem", author=regular_user)
```

Domyślny `scope` to `function` — każdy test dostaje świeży obiekt, testy się nie zanieczyszczają. Fixtures używane w wielu plikach przenosimy do `tests/conftest.py` (nie importuje się go ręcznie — pytest wykrywa go automatycznie).

> [!WARNING]
> Fixture nie powinna wykonywać głównej akcji testu (np. od razu zamykać zgłoszenie) — powinna tylko przygotować stan. Jeśli fixture ukrywa to, co test właściwie sprawdza, jest zbyt rozbudowana.

## 11. Coverage

```bash
pytest --cov=knowledge_app --cov-report=term-missing
pytest --cov=knowledge_app --cov-branch --cov-report=term-missing   # + branch coverage
```

Coverage pokazuje, które linie/gałęzie zostały **wykonane** przez testy — nie mówi, czy testy sprawdziły **poprawne** zachowanie:

```python
# Słaby test — zwiększa coverage, nic nie potwierdza
def test_can_manage_documents() -> None:
    user = User(email="agent@example.com", role="agent")
    user.can_manage_documents()

# Lepszy test
def test_active_agent_can_manage_documents() -> None:
    user = User(email="agent@example.com", role="agent")
    assert user.can_manage_documents() is True
```

Orientacyjny cel na koniec soboty: line coverage ≥ 80%, branch coverage ≥ 70% — ale ważniejsze jest pokrycie reguł biznesowych niż sam procent.

---

# Niedziela — jakość kodu i CI

Niedziela **kontynuuje tę samą domenę** co sobota (`User`, `Document`, `SupportTicket`), dokańcza klasę `KnowledgeBase` (w sobotę zwykle zadanie domowe) i dokłada do niej pełny workflow jakości.

## 12. Organizacja testów w większym projekcie

Gdy domena rośnie do kilku modułów, testy dzielimy według modułów aplikacji:

```text
src/knowledge_app/          tests/
├── users.py           →    test_users.py
├── documents.py        →    test_documents.py
├── support.py           →    test_support.py
└── knowledge_base.py     →    test_knowledge_base.py
tests/conftest.py  — fixtures współdzielone między plikami
```

Zasady:

- jeden test sprawdza jedno zachowanie,
- testy są niezależne — żaden nie zakłada, że inny uruchomił się wcześniej,
- nazwa testu opisuje warunek i oczekiwany rezultat,
- fixture zależna od innej fixture (np. `knowledge_base_with_documents(sample_document)`) jest naturalna — pytest sam rozwiąże zależności.

## 13. `pytest.approx` dla liczb zmiennoprzecinkowych

Pierwsza metoda w naszej domenie zwracająca `float` (np. `KnowledgeBase.tag_coverage` — odsetek dokumentów z danym tagiem) wymaga ostrożnego porównania:

```python
import pytest

def test_tag_coverage_returns_expected_ratio(knowledge_base_with_documents) -> None:
    result = knowledge_base_with_documents.tag_coverage("python")

    assert result == pytest.approx(2 / 3)
```

Bezpośrednie `==` na wynikach zmiennoprzecinkowych bywa zawodne z powodu sposobu reprezentowania liczb przez komputer — `pytest.approx` porównuje z niewielką, rozsądną tolerancją.

## 14. Testowanie zachowania, nie implementacji

```python
def test_calculate_shipping_returns_zero_for_order_at_threshold() -> None:
    assert calculate_shipping(200) == 0
```

Test nie interesuje się tym, czy w środku jest `if`, `match`, słownik czy inna implementacja — sprawdza wynik. Dzięki temu można bezpiecznie refaktoryzować kod bez przepisywania testów.

## 15. Black — formatowanie kodu

```bash
black --check src tests      # tylko sprawdza — używamy w CI
black src tests               # formatuje pliki
```

Black ujednolica wygląd kodu (łamanie linii, spacje, wcięcia) i kończy dyskusje o stylu w zespole. Nie sprawdza logiki biznesowej i nie zastępuje testów ani code review. Po uruchomieniu zawsze sprawdź `git diff`.

## 16. Ruff — linting kodu

```bash
ruff check src tests           # analiza
ruff check src tests --fix     # automatyczne poprawki (nieużywane importy, kolejność importów...)
```

Ruff wykrywa m.in. nieużywane importy i zmienne, złą kolejność importów, ryzykowne konstrukcje. Po `--fix` zawsze sprawdź `git diff` i uruchom testy ponownie.

| Narzędzie | Rola |
|---|---|
| Black | formatuje kod |
| Ruff | analizuje kod i wykrywa problemy |
| pytest | sprawdza zachowanie |

## 17. `pyproject.toml`

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
addopts = "-ra"

[tool.coverage.run]
source = ["knowledge_app"]
branch = true

[tool.coverage.report]
show_missing = true

[tool.black]
line-length = 88
target-version = ["py312"]

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "B"]   # E: styl, F: błędy/importy, I: kolejność importów, B: bugbear
```

> [!IMPORTANT]
> Cały kurs, od Weekend 5, stoi na Pythonie 3.12 — `target-version` w Ruffu/Black i `python-version` w CI muszą się z tym zgadzać.

## 18. pre-commit

`pre-commit` uruchamia wybrane sprawdzenia **przed** wykonaniem commita — łapie problem, zanim trafi do repozytorium.

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.10.0
    hooks:
      - id: black

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.4
    hooks:
      - id: ruff
        args: ["--fix"]
      - id: ruff-format
```

```bash
pip install pre-commit
pre-commit install              # instaluje hooki lokalnie w .git/hooks
pre-commit run --all-files      # uruchamia ręcznie na całym repo
```

Typowy przebieg: `git commit` → hook poprawia plik → **commit zostaje przerwany** → `git status` / `git diff` → `git add .` → `git commit` ponownie. To normalne — pre-commit właśnie wykonał swoją pracę, nie zepsuł projektu.

## 19. CI i GitHub Actions

**CI (Continuous Integration)** to automatyczne sprawdzanie projektu w **czystym środowisku** po `push`/`pull_request` — wykrywa problemy, które lokalnie są niewidoczne (niezacommitowany plik, inna wersja Pythona, brakująca zależność).

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
  pull_request:

jobs:
  quality:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt

      - name: Run Ruff
        run: ruff check src tests

      - name: Run Black check
        run: black --check src tests

      - name: Run tests with coverage
        run: pytest --cov=knowledge_app --cov-report=term-missing
```

Zielony pipeline oznacza tylko, że **zdefiniowane kontrole przeszły** — nie gwarantuje braku wszystkich błędów ani pełnego pokrycia testami.

## 20. Jak czytać błędy z CI?

1. Otwórz zakładkę **Actions**, wybierz nieudane uruchomienie.
2. Znajdź **pierwszy** czerwony krok — kolejne błędy bywają tylko jego skutkiem.
3. Przeczytaj log tego kroku od końca.
4. Uruchom to samo polecenie **lokalnie** (`ruff check ...`, `black --check ...`, `pytest ...`).
5. Popraw przyczynę, uruchom pełną kontrolę lokalną, zrób commit i push ponownie.

## 21. AI jako pomocnik

AI może pomóc zaproponować przypadki testowe, wyjaśnić komunikat błędu pytest lub log CI, ocenić czytelność nazwy testu. AI nie zna pełnych wymagań projektu — może wymyślić nieistniejącą funkcję, założyć inną regułę biznesową albo przetestować implementację zamiast zachowania.

Przykładowy prompt:

```text
Przeanalizuj klasę KnowledgeBase: add_document, get_document, find_by_tag, tag_coverage.
Reguły: document_id musi być unikalny, get_document zgłasza LookupError gdy brak
dokumentu, tag_coverage zwraca 0.0 dla pustej bazy.
Zaproponuj maksymalnie 6 przypadków testowych. Nie pisz kodu.
Przy każdym wskaż testowaną regułę.
```

Każdą propozycję oceń jako: zgodna z wymaganiami / niezgodna / wymaga doprecyzowania / wartościowa poza zakresem. Zasada: **AI może zaproponować, programista musi zweryfikować.**

## 22. Szybka ściąga komend

```bash
# pytest
pytest -v
pytest -k deactivate
pytest --cov=knowledge_app --cov-report=term-missing

# jakość kodu
black --check src tests
ruff check src tests --fix

# pre-commit
pre-commit install
pre-commit run --all-files

# pełny lokalny cykl przed pushem
pytest --cov=knowledge_app --cov-report=term-missing && \
ruff check src tests && \
black --check src tests && \
pre-commit run --all-files
```

## 23. Podsumowanie

Po tym weekendzie projekt ma pierwszy realny fundament jakości: klasy domenowe z walidacją, testy pokrywające happy path i błędy, oraz automatyczną kontrolę formatowania, lintingu i testów — lokalnie i w CI.

> [!IMPORTANT]
> Dobry projekt to nie tylko kod, który działa. To kod, który można automatycznie sprawdzić — i który faktycznie jest sprawdzany, zanim trafi do głównej gałęzi.

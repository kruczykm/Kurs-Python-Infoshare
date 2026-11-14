# 🧩 Capstone — Weekend 4: testy, klasy domenowe i CI w `ai-knowledge-desk`

> **Kurs:** AI Python Engineer
> **Blok:** Weekend 4 — jakość, testy i CI
> **Projekt:** `ai-knowledge-desk`

---

## Kontekst

Po Weekend 3 `ai-knowledge-desk` ma tylko rozbity na moduły `akd_cli` (`io_utils.py`, `parsing.py`, `reporting.py`) i type hints w kluczowych funkcjach — brak jeszcze klas domenowych i brak jakiejkolwiek automatycznej kontroli jakości; teraz dokładamy pierwsze klasy biznesowe (na razie w pamięci, bez bazy danych — to przygotowanie pod modele Django z Weekend 6) oraz pełny lokalny i CI-owy workflow testów i jakości kodu.

---

## Co dochodzi do projektu

| Element | Opis |
|---|---|
| Klasy domenowe | `User`, `AdminUser(User)`, `Document`, `KnowledgeBase`, `SupportTicket` — proste klasy z `__init__`, atrybutami, metodami, walidacją i lekkim dziedziczeniem |
| Testy klas domenowych | pytest: happy path + edge case dla każdej klasy, w tym `pytest.raises` i `@pytest.mark.parametrize` |
| Testy `akd_cli` | pierwsze testy jednostkowe modułów z Weekend 2–3 (`io_utils.py`, `parsing.py`, `reporting.py`) — happy path + obsługa błędów |
| Coverage | `pytest-cov` uruchamiane lokalnie, raport `term-missing` |
| `pyproject.toml` | konfiguracja `pytest`, `coverage`, `black`, `ruff` |
| `requirements-dev.txt` | `pytest`, `pytest-cov`, `black`, `ruff`, `pre-commit` |
| `.pre-commit-config.yaml` | hooki Black i Ruff uruchamiane przed każdym commitem |
| `.github/workflows/ci.yml` | pipeline GitHub Actions: lint (Ruff) + format check (Black) + testy + coverage, Python 3.12 |

---

## Kroki

1. **Zaprojektuj klasy domenowe** w `akd_cli/` (lub nowym pakiecie `knowledge_app/` obok niego): `User` (email, rola z `{user, agent, admin}`, `is_active`, `deactivate()`, `can_manage_documents()`), `AdminUser(User)`, `Document` (tytuł, treść, lista tagów per-instancja, `add_tag()`), `KnowledgeBase` (kolekcja dokumentów: `add_document`, `get_document` → `LookupError`, `find_by_tag`), `SupportTicket` (autor, priorytet, status, komentarze, `add_comment()`, `close()`).
2. **Zwaliduj dane w konstruktorach** — pusty e-mail/tytuł, niedozwolona rola/priorytet, nieaktywny autor zgłoszenia powinny zgłaszać `ValueError`; brakujący dokument w `KnowledgeBase.get_document` — `LookupError`.
3. **Napisz testy klas domenowych** w `tests/` — minimum 12 testów łącznie, w tym min. 3 testy wyjątków (`pytest.raises`), min. 1 test parametryzowany (np. role albo priorytety) i min. 2 fixtures (jedna zależna od drugiej, np. `support_ticket` korzystające z `regular_user`).
4. **Dopisz testy do `akd_cli`** z Weekend 2–3 — wybierz 2–3 funkcje (np. parsowanie, liczenie statystyk, obsługę błędu braku pliku) i pokryj je testami happy path + błąd.
5. **Uruchom coverage** (`pytest --cov=<pakiet> --cov-report=term-missing`) i zapisz wynik oraz jedną rzecz do dopisania później.
6. **Dodaj `pyproject.toml`** z konfiguracją `pytest` (`testpaths`, `pythonpath`), `coverage` (`source`, `branch = true`) oraz `[tool.black]` i `[tool.ruff]` (`line-length = 88`, `target-version = "py312"`, `select = ["E", "F", "I", "B"]`).
7. **Uruchom lokalnie i popraw** `black --check .`, `ruff check .`.
8. **Dodaj `.pre-commit-config.yaml`** (hooki `black` i `ruff`/`ruff-format`), zainstaluj (`pre-commit install`) i uruchom na całym repo (`pre-commit run --all-files`).
9. **Dodaj `.github/workflows/ci.yml`** uruchamiany na `push` i `pull_request`: checkout → setup Python 3.12 → instalacja `requirements-dev.txt` → `ruff check` → `black --check` → `pytest --cov`.
10. **Wypchnij zmiany i sprawdź**, że workflow w zakładce Actions jest zielony; jeśli nie — zdiagnozuj pierwszy czerwony krok, popraw lokalnie, wypchnij ponownie.

---

## Definition of Done

- [ ] `User`, `AdminUser`, `Document`, `KnowledgeBase`, `SupportTicket` istnieją i mają walidację kluczowych pól.
- [ ] Projekt ma katalog `tests/` z minimum 12 testami klas domenowych + testami wybranych funkcji `akd_cli`.
- [ ] Co najmniej 3 testy używają `pytest.raises`, co najmniej 1 jest sparametryzowany, co najmniej 2 korzystają z fixtures.
- [ ] `pytest` przechodzi lokalnie; coverage uruchamia się i został krótko przeanalizowany.
- [ ] `pyproject.toml` zawiera konfigurację `pytest`, `coverage`, `black` i `ruff`.
- [ ] `black --check .` i `ruff check .` przechodzą lokalnie.
- [ ] `.pre-commit-config.yaml` istnieje, `pre-commit run --all-files` przechodzi.
- [ ] `.github/workflows/ci.yml` istnieje, uruchamia lint + format check + testy + coverage na Pythonie 3.12.
- [ ] Ostatni workflow na GitHubie jest zielony (albo błąd jest jasno opisany w notatce do zadania).

---

## Co dopisać do README

Do głównego `README.md` projektu `ai-knowledge-desk` dopisz sekcję:

```markdown
## Jakość kodu i testy

Klasy domenowe: `User`, `AdminUser`, `Document`, `KnowledgeBase`, `SupportTicket` (`akd_cli/` lub `knowledge_app/`).

Uruchomienie testów i kontroli jakości:

\`\`\`bash
pip install -r requirements-dev.txt
pytest --cov=akd_cli --cov-report=term-missing
black --check .
ruff check .
pre-commit run --all-files
\`\`\`

CI: GitHub Actions (`.github/workflows/ci.yml`) uruchamia lint, format check, testy i coverage na każdym push/PR.
```

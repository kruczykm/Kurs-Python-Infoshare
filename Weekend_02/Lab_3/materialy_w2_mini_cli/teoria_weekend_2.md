# 📚 Weekend 2 — Python: pliki, wyjątki, mini-CLI

> **Teoria do bloku**  
> Kurs: **AI Python Engineer**  
> Temat: **operacje na plikach tekstowych, obsługa wyjątków (`try/except`) oraz początkujące mini-CLI (`sys.argv`)**  
> Poziom: **1/5 (Początkujący)**  
> Cel: opanowanie podstawowych mechanizmów czytania/zapisu danych na dysku, kontrolowania błędów oraz uruchamiania prostych skryptów z argumentami z terminala.

---

## 🧭 O czym jest ta teoria?

W tym bloku robimy pierwszy krok poza czysty interpreter Pythona i dane trzymane wyłącznie w pamięci RAM:
1. **Praca z plikami tekstowymi** — jak bezpiecznie otworzyć plik za pomocą menedżera kontekstu `with open(...)`, odczytać jego zawartość (`.read()`, `.readlines()`) i dopisać nową treść w trybie append (`"a"`).
2. **Wyjątki i błędy (`try`, `except`)** — jak radzić sobie z sytuacjami, gdy plik nie istnieje (`FileNotFoundError`), użytkownik poda złe dane lub wystąpi błąd systemowy, zamiast doprowadzić do awarii programu.
3. **Początkujące mini-CLI (`sys.argv`)** — jak przyjmować parametry wprost z linii poleceń (np. `python script.py odczytaj notatka.txt`) i sterować zachowaniem skryptu.

---

## 1. Operacje na plikach tekstowych (`open`)

W Pythonie do otwarcia pliku służy wbudowana funkcja `open()`. Zawsze zaleca się stosowanie menedżera kontekstu `with`, ponieważ automatycznie zamyka on plik po zakończeniu bloku kodu (zapobiega to wyciekom zasobów i blokowaniu plików w systemie).

```python
# Odczyt pliku tekstowego
with open("notatki.txt", "r", encoding="utf-8") as f:
    zawartosc = f.read()
    print(zawartosc)

# Dopisywanie do pliku (tryb 'a' - append)
with open("notatki.txt", "a", encoding="utf-8") as f:
    f.write("Nowa linijka notatki\n")
```

---

## 2. Obsługa wyjątków (`try ... except`)

Gdy plik nie istnieje lub nie mamy do niego dostępu, Python zgłasza wyjątek (np. `FileNotFoundError`). Aby program nie przerywał działania nagłym tracebackiem, używamy konstrukcji `try/except`:

```python
try:
    with open("nieznany_plik.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Błąd: Taki plik nie istnieje!")
```

---

## 3. Początkujące mini-CLI (`sys.argv`)

Wielkie narzędzia CLI używają zaawansowanego `argparse` (którego uczymy się w późniejszych blokach), ale na samym starcie  najprostszą metodą przyjmowania argumentów z terminala jest lista `sys.argv` z modułu `sys`.

- `sys.argv[0]` to nazwa uruchamianego skryptu.
- `sys.argv[1]`, `sys.argv[2]` itd. to kolejne argumenty wpisane w terminalu po spacji.

Przykład wywołania w terminalu:
```bash
python notes_cli.py read dziennik.txt
```

Kod w skrypcie:
```python
import sys

if len(sys.argv) > 1:
    komenda = sys.argv[1]
    argument = sys.argv[2]
    print(f"Wykonuję komendę: {komenda} dla pliku {argument}")
```

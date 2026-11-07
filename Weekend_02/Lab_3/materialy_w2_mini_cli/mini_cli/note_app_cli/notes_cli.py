from pathlib import Path
import sys

def read_note_file(file_path: str | Path) -> str | None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Błąd: Plik '{file_path}' nie istnieje!")
        return None

def append_note(file_path: str | Path, new_line: str) -> bool:
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"\n{new_line}")
            return True
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu: {e}")
        return False

def count_lines(content_file: str) -> int:
    return len(content_file.splitlines())

def handle_command(args: list[str]) -> str:
    # Router komend: sprawdza, czy podano wystarczającą liczbę argumentów
    if len(args) < 2:
        return "Błąd: Brak wymaganych argumentów."

    action = args[0]   # Pierwszy argument to akcja (np. read, count, append)
    filepath = args[1] # Drugi argument to ścieżka do pliku

    # Obsługa specyficzna dla zapisu (wymaga dodatkowego argumentu z tekstem)
    if action == "append":
        if len(args) < 3:
            return "Błąd: Podaj tekst do dopisania!"
        text_to_add = args[2]
        success = append_note(filepath, text_to_add)
        if success:
            return "Notatka została pomyślnie dopisana!"
        return "Nie udało się dopisać notatki."

    # Dla operacji odczytu i zliczania najpierw pobieramy zawartość pliku
    content = read_note_file(filepath)
    if content is None:
        return "Nie można wykonać operacji z powodu błędu pliku."

    # Rozgałęzienie logiki na podstawie wybranej akcji
    if action == "read":
        return content
    elif action == "count":
        return f"Liczba linijek w pliku: {count_lines(content)}"
    else:
        return f"Nieznana akcja: {action}"

def main():
    # Pobieramy argumenty przekazane z terminala (odcinając nazwę samego skryptu)
    args = sys.argv[1:]

    # Jeśli użytkownik podał za mało argumentów, wyświetlamy pomoc i przerywamy działanie
    if len(args) < 2:
        print("Użycie:")
        print("  python notes_cli.py read <plik>")
        print("  python notes_cli.py count <plik>")
        print("  python notes_cli.py append <plik> \"Tekst\"")
        sys.exit(1)

    # Przekazujemy argumenty do funkcji zarządządzającej i wypisujemy wynik w konsoli
    result = handle_command(args)
    print(result)

# Punkt wejścia dla generowanego skryptu
if __name__ == "__main__":
    main()

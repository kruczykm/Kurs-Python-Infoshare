"""
Moduł: data.py
---------------
Serce logiki biznesowej całego programu (przetwarzanie danych w pamięci).
Moduł ten NIE wykonuje operacji na dysku (nie skanuje folderów, nie zapisuje plików).
Jego jedynym zadaniem jest przyjmowanie przygotowanych danych i wykonywanie na nich obliczeń.

Główne elementy modułu:
1. Kontrakty typów (TypedDict):
   - FileInfo: Szablon słownika opisującego pojedynczy plik (ścieżka, rozszerzenie, rozmiar). -> opisuje pojedynczy plik
   - AuditSummary: Szablon słownika opisującego pełne podsumowanie audytu folderu. -> opisuje końcowy raport audytu

2. Dane testowe:
   - SAMPLE_FILES: Sztuczna, przykładowa lista plików w pamięci służąca do testowania kodu.

3. Funkcje analityczne i przetwarzające (do napisania w TODO):
   - unique_extensions: Zwraca zbiór unikalnych rozszerzeń.
   - count_extensions: Zlicza, ile plików ma każde rozszerzenie.
   - total_size: Sumuje łączny rozmiar wszystkich plików w bajtach.
   - largest_files: Wybiera i sortuje największe pliki z ograniczeniem do limitu.
   - build_summary: Łączy powyższe wyniki w jeden gotowy raport (AuditSummary).
"""

# imortujemy TypedDict z modułu typing, aby zdefiniować struktury danych dla plików i podsumowania audytu.
from typing import TypedDict

class FileInfo(TypedDict):
    path: str
    extension: str
    size_bytes: int

class AuditSummary(TypedDict):
    file_count: int
    total_size_bytes: int
    extension_counts: dict[str, int]
    largest_files: list[FileInfo]

# Przykładowe dane testowe trzymane w pamięci.
SAMPLE_FILES: list[FileInfo] = [
    {"path": "notes/todo.txt", "extension": ".txt", "size_bytes": 1200},
    {"path": "notes/ideas.txt", "extension": ".txt", "size_bytes": 800},
    {"path": "data/users.csv", "extension": ".csv", "size_bytes": 2500},
    {"path": "README", "extension": "[no extension]", "size_bytes": 300},
]


def unique_extensions(files: list[FileInfo]) -> set[str]:
    """Return the set of extensions found in ``files``.
    For SAMPLE_FILES the result contains ``.txt``, ``.csv``, and
    ``[no extension]``.
    """
    
    # 1. Tworzymy pusty zbiór (set).
    # Automatycznie odrzuca duplikaty – każde rozszerzenie pojawi się tu tylko raz.
    extensions = set()
    
    # 2. Przechodzimy pętlą przez każdy plik na liście
    for file in files:
        # 3. Wyciągamy rozszerzenie bieżącego pliku i dodajemy je do zbioru.
        # Jeśli rozszerzenie już tam jest, Python po prostu zignoruje tę próbę.
        extensions.add(file["extension"])
    # 4. Zwracamy gotowy, unikalny zbiór na zewnątrz funkcji
    return extensions

    
def count_extensions(files: list[FileInfo]) -> dict[str, int]:
    """Return a mapping of extension to number of files.
    Expected result for SAMPLE_FILES::
    {".txt": 2, ".csv": 1, "[no extension]": 1}
    """
    
    # 1. Tworzymy pusty słownik, który będzie przechowował wyniki zliczania
    # (klucz: rozszerzenie pliku, wartość: liczba wystąpień)
    extension_counts = {}

    # 2. Przechodzimy pętlą przez każdy plik na liście
    for file in files:
        # Wyciągamy rozszerzenie z bieżącego pliku
        extension_value = file["extension"]
        # 3. Metoda .get():
        # - Jeśli rozszerzenie już jest w słowniku, .get() pobiera jego obecną wartość.
        # - Jeśli go jeszcze nie ma, .get() zwraca domyślne 0.
        # Następnie do tej wartości dodajemy 1 i zapisujemy z powrotem w słowniku.
        extension_counts[extension_value] = extension_counts.get(extension_value, 0) + 1

    # 4. Zwracamy gotowy, w pełni uzupełniony słownik z podsumowaniem    
    return extension_counts


def total_size(files: list[FileInfo]) -> int:
    """Return the combined size in bytes.

    The result is 4800 for SAMPLE_FILES and 0 for an empty list.
    """
    
    # 1. Tworzymy zmienną "akumulator" startującą od zera.
    # Jeśli lista plików będzie pusta, pętla się nie wykona i funkcja zwróci właśnie to 0.
    total = 0
    
    # 2. Przechodzimy pętlą przez każdy plik na liście
    for file in files:
        # 3. Pobieramy rozmiar bieżącego pliku ("size_bytes") i dodajemy go do naszej sumy.
        total += file["size_bytes"]

    # 4. Zwracamy ostateczną, całkowitą sumę rozmiarów w bajtach
    return total


def largest_files(files: list[FileInfo], limit: int) -> list[FileInfo]:
    """Return at most ``limit`` files, ordered from largest to smallest.

    Do not modify the input list. Return an empty list when ``limit <= 0``.
    For ``largest_files(SAMPLE_FILES, 2)``, ``data/users.csv`` comes first and
    ``notes/todo.txt`` comes second.
    """
    
    # 1. Sprawdzamy przypadek brzegowy: jeśli limit jest zerowy lub ujemny, zwracamy pustą listę
    if limit <= 0:
        return []
        
    # 2. Tworzymy posortowaną kopie listy malejąco po rozmiarze ("size_bytes"), 
    # - sorted() nie modyfikuje oryginału (tworzy nową listę),
    # - reverse=True ustawia kolejność malejącą (od największego),
    # - key=lambda f: f[...] wybiera "size_bytes" jako pole do porównania,lambda mala fukcja, ktora mowi Pythonowi :
    #   bierz po kolei elementy i wyciągaj z nich tylko tę jedną rzecz”
    sorted_files = sorted(files, key=lambda f: f["size_bytes"], reverse=True)
    
    # 3. Zwracamy wycinek listy od początku do wartości `limit`. 
    # Jeśli limit jest większy niż liczba plików, Python automatycznie weźmie tyle, ile jest.
    return sorted_files[:limit]


def build_summary(files: list[FileInfo], top: int = 5) -> AuditSummary:
    """Build one JSON-serializable summary from the earlier functions."""
    
    summary: AuditSummary = {
        "total_files": len(files),
        "total_size_bytes": total_size(files),
        "unique_extensions": list(unique_extensions(files)),
        "extension_counts": count_extensions(files),
        "largest_files": largest_files(files, top)
    } 
    return summary


if __name__ == "__main__":
    print("Start with TODO 1. Expected results are documented above each task.")
    # Test
    summary = build_summary(SAMPLE_FILES, 2)
    print(summary)


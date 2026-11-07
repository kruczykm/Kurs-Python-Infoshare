# 🧩 Capstone — Menedżer Notatek (Mini-CLI)

## Cel
Stworzyć prosty skrypt oparty na plikach tekstowych i obsłudze wyjątków, który po uruchomieniu z terminala pozwala na zarządzanie prostym dziennikiem notatek.

## Wymagania (Definition of Done dla początkujących)
1. Program korzysta wyłącznie z biblioteki standardowej (`sys`, `pathlib` lub zwykły `open`).
2. Bezpiecznie obsługuje brak pliku za pomocą `try/except FileNotFoundError`.
3. Pozwala na wykonanie akcji odczytu (`read`) oraz dopisywania (`add`) przekazanych jako argumenty w terminalu.
4. Zwraca kod wyjścia `0` przy sukcesie oraz `1` lub `2` w przypadku błędów argumentów lub braku pliku.

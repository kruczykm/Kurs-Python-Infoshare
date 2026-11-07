"""
Pakiet: folder_audit
-------------------
Ten plik (__init__.py) sprawia, że katalog 'folder_audit' jest traktowany
przez Pythona jako pakiet (paczka modułów), który zawiera logikę narzędzia CLI.

Dzięki niemu możliwe jest:
1. Wzajemne importowanie kodu między plikami tego projektu (cli.py, files.py itp.).
2. Uruchamianie całego narzędzia z poziomu terminala za pomocą polecenia:
   python -m exercises.folder_audit <ścieżka_do_folderu>
"""

# A read-only folder auditing tool.

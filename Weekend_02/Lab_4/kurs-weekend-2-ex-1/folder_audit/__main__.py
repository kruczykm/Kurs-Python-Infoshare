# Główny punkt startowy. To tutaj program startuje, gdy wpisujesz w terminalu python -m exercises.folder_audit.
# Łączy ze sobą działanie CLI oraz logiki skanującej.

from folder_audit.cli import main

raise SystemExit(main())

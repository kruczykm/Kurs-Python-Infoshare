"""Part 2: scanning directories and writing files.

Use only the standard library. Let operating-system errors propagate for now;
they will be translated into friendly errors in Part 3.
"""

from pathlib import Path

from folder_audit.data import AuditSummary, FileInfo


PathLike = str | Path
NO_EXTENSION = "[no extension]"


def scan_folder(folder: PathLike, include_hidden: bool = False) -> list[FileInfo]:
    """Recursively collect information about regular files in ``folder``.

    TODO 1:
    - use ``Path.rglob("*")``;
    - include regular files only and skip symbolic links;
    - unless ``include_hidden`` is true, skip a path when any of its relative
      parts starts with ``.``;
    - store paths relative to ``folder`` and use forward slashes;
    - normalize extensions to lowercase;
    - use ``NO_EXTENSION`` when ``Path.suffix`` is empty;
    - get each size from ``Path.stat()``;
    - return records sorted by their relative path.

    Do not catch OSError in this function.
    """
    raise NotImplementedError


def save_json_report(summary: AuditSummary, destination: PathLike) -> None:
    """Write ``summary`` as readable UTF-8 JSON.

    TODO 2:
    - create the destination's parent directories when needed;
    - use ``json.dump`` with an indentation of two spaces;
    - add a final newline to the file.
    """
    raise NotImplementedError

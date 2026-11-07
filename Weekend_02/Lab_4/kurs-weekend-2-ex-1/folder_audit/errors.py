"""Part 3: validating input and translating exceptions."""

from pathlib import Path

from folder_audit.data import FileInfo
from folder_audit.files import PathLike, scan_folder


class FolderAuditError(Exception):
    """Base class for errors that can be shown directly to the user."""


class FolderNotFoundError(FolderAuditError):
    """The requested path does not exist."""


class InvalidFolderError(FolderAuditError):
    """The requested path exists but is not a directory."""


class FolderAccessError(FolderAuditError):
    """The operating system refused access while scanning."""


def validate_folder(folder: PathLike) -> Path:
    """Return a normalized directory path or raise a specific error.

    TODO 1:
    - convert the input to Path and expand ``~``;
    - raise FolderNotFoundError if it does not exist;
    - raise InvalidFolderError if it is not a directory;
    - include the path in every error message.
    """
    raise NotImplementedError


def scan_folder_safely(
    folder: PathLike, include_hidden: bool = False
) -> list[FileInfo]:
    """Validate and scan a folder, translating expected OS errors.

    TODO 2:
    - call ``validate_folder`` first;
    - call ``scan_folder`` inside try/except;
    - translate PermissionError into FolderAccessError;
    - translate other OSError instances into FolderAuditError;
    - preserve the original exception with ``raise ... from error``;
    - do not use ``except Exception``.
    """
    raise NotImplementedError

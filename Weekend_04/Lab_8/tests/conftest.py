import pytest

from knowledge_app.documents import Document
from knowledge_app.support import SupportTicket
from knowledge_app.users import User


@pytest.fixture
def regular_user() -> User:
    return User(email="user@example.com")


@pytest.fixture
def sample_document() -> Document:
    return Document(
        document_id=1,
        title="Resetowanie hasła",
        content="Instrukcja resetowania hasła.",
    )


@pytest.fixture
def support_ticket(
    regular_user: User,
) -> SupportTicket:
    return SupportTicket(
        ticket_id=1,
        title="Problem z logowaniem",
        author=regular_user,
    )

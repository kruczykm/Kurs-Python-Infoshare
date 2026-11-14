import pytest

from knowledge_app.users import User


def test_user_is_active_after_creation() -> None:
    # Arrange
    user = User(email="anna@example.com")

    # Act
    result = user.is_active

    # Assert
    assert result is True


def test_deactivate_changes_user_status() -> None:
    user = User(email="anna@example.com")

    user.deactivate()

    assert user.is_active is False


def test_user_rejects_empty_email() -> None:
    with pytest.raises(
        ValueError,
        match="Email cannot be empty",
    ):
        User(email="")


def test_user_rejects_unsupported_role() -> None:
    with pytest.raises(
        ValueError,
        match="Unsupported role",
    ):
        User(
            email="hero@example.com",
            role="superhero",
        )


@pytest.mark.parametrize(
    ("role", "expected"),
    [
        ("user", False),
        ("agent", True),
        ("admin", True),
    ],
)
def test_can_manage_documents_depends_on_role(
    role: str,
    expected: bool,
) -> None:
    user = User(
        email="person@example.com",
        role=role,
    )

    assert user.can_manage_documents() is expected


@pytest.mark.parametrize(
    "email",
    ["", " ", "   "],
    ids=["empty", "single-space", "multiple-spaces"],
)
def test_user_rejects_blank_email(email: str) -> None:
    with pytest.raises(ValueError):
        User(email=email)


def test_inactive_agent_cannot_manage_documents() -> None:
    user = User(
        email="agent@example.com",
        role="agent",
    )
    user.deactivate()

    assert user.can_manage_documents() is False

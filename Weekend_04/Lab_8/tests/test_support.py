import pytest

from knowledge_app.support import SupportTicket
from knowledge_app.users import User


def test_ticket_has_expected_initial_state(
    support_ticket: SupportTicket,
) -> None:
    assert support_ticket.status == "open"
    assert support_ticket.priority == "medium"
    assert support_ticket.comments == []


def test_add_comment_adds_normalized_comment(
    support_ticket: SupportTicket,
) -> None:
    support_ticket.add_comment("  Problem nadal występuje.  ")

    assert support_ticket.comments == ["Problem nadal występuje."]


def test_add_comment_rejects_blank_comment(
    support_ticket: SupportTicket,
) -> None:
    with pytest.raises(
        ValueError,
        match="Comment cannot be empty",
    ):
        support_ticket.add_comment("   ")


def test_close_changes_ticket_status(
    support_ticket: SupportTicket,
) -> None:
    support_ticket.close()

    assert support_ticket.status == "closed"


def test_close_rejects_already_closed_ticket(
    support_ticket: SupportTicket,
) -> None:
    support_ticket.close()

    with pytest.raises(
        ValueError,
        match="Ticket is already closed",
    ):
        support_ticket.close()


@pytest.mark.parametrize(
    "priority",
    ["low", "medium", "high"],
)
def test_ticket_accepts_supported_priority(
    regular_user: User,
    priority: str,
) -> None:
    ticket = SupportTicket(
        ticket_id=1,
        title="Problem",
        author=regular_user,
        priority=priority,
    )

    assert ticket.priority == priority


@pytest.mark.parametrize(
    "priority",
    ["urgent", "critical", ""],
)
def test_ticket_rejects_unsupported_priority(
    regular_user: User,
    priority: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="Unsupported priority",
    ):
        SupportTicket(
            ticket_id=1,
            title="Problem",
            author=regular_user,
            priority=priority,
        )


def test_ticket_rejects_blank_title(
    regular_user: User,
) -> None:
    with pytest.raises(
        ValueError,
        match="Title cannot be empty",
    ):
        SupportTicket(
            ticket_id=1,
            title="   ",
            author=regular_user,
        )


def test_ticket_rejects_inactive_author() -> None:
    user = User(email="user@example.com")
    user.deactivate()

    with pytest.raises(
        ValueError,
        match="Author must be active",
    ):
        SupportTicket(
            ticket_id=1,
            title="Problem",
            author=user,
        )

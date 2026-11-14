from knowledge_app.users import User


class SupportTicket:
    ALLOWED_PRIORITIES = {"low", "medium", "high"}

    def __init__(
        self,
        ticket_id: int,
        title: str,
        author: User,
        priority: str = "medium",
    ) -> None:
        if not title.strip():
            raise ValueError("Title cannot be empty")

        if not author.is_active:
            raise ValueError("Author must be active")

        if priority not in self.ALLOWED_PRIORITIES:
            raise ValueError("Unsupported priority")

        self.ticket_id = ticket_id
        self.title = title
        self.author = author
        self.priority = priority
        self.status = "open"
        self.comments: list[str] = []

    def add_comment(self, comment: str) -> None:
        normalized_comment = comment.strip()

        if not normalized_comment:
            raise ValueError("Comment cannot be empty")

        self.comments.append(normalized_comment)

    def close(self) -> None:
        if self.status == "closed":
            raise ValueError("Ticket is already closed")

        self.status = "closed"

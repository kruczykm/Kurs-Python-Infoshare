class User:
    ALLOWED_ROLES = {"user", "agent", "admin"}

    def __init__(self, email: str, role: str = "user") -> None:
        if not email.strip():
            raise ValueError("Email cannot be empty")

        if role not in self.ALLOWED_ROLES:
            raise ValueError("Unsupported role")

        self.email = email
        self.role = role
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False

    def can_manage_documents(self) -> bool:
        return self.is_active and self.role in {"agent", "admin"}


class AdminUser(User):
    def __init__(self, email: str) -> None:
        super().__init__(email=email, role="admin")

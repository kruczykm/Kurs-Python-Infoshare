class User:
    def __init__(self, email: str, role: str = "user") -> None:
        self.email = email
        self.role = role
        self.is_active = True

    def deactivate(self) -> None:
        # Zmień stan obiektu.
        self.is_active = False

    def can_manage_documents(self) -> bool:
        # Zwróć True dla aktywnego agenta lub administratora.
        if self.is_active and self.role in {"agent", "admin"}:
            return True
        else:
            return False


class AdminUser(User):
    def __init__(self, email: str) -> None:
        super().__init__(email=email, role="admin")
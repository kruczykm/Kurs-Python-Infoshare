class Document:
    def __init__(
        self,
        document_id: int,
        title: str,
        content: str,
    ) -> None:
        if not title.strip():
            raise ValueError("Title cannot be empty")

        if not content.strip():
            raise ValueError("Content cannot be empty")

        self.document_id = document_id
        self.title = title
        self.content = content
        self.tags: list[str] = []

    def add_tag(self, tag: str) -> None:
        normalized_tag = tag.strip().lower()

        if not normalized_tag:
            raise ValueError("Tag cannot be empty")

        if normalized_tag not in self.tags:
            self.tags.append(normalized_tag)

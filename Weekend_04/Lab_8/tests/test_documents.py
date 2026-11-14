import pytest

from knowledge_app.documents import Document


def test_document_starts_without_tags(
    sample_document: Document,
) -> None:
    assert sample_document.tags == []


def test_add_tag_changes_document(
    sample_document: Document,
) -> None:
    sample_document.add_tag("python")

    assert sample_document.tags == ["python"]


def test_fixture_returns_fresh_document(
    sample_document: Document,
) -> None:
    assert sample_document.tags == []


def test_add_tag_normalizes_value(
    sample_document: Document,
) -> None:
    sample_document.add_tag("  Python  ")

    assert sample_document.tags == ["python"]


def test_add_tag_does_not_add_duplicate(
    sample_document: Document,
) -> None:
    sample_document.add_tag("Python")
    sample_document.add_tag("python")

    assert sample_document.tags == ["python"]


def test_add_tag_rejects_blank_value(
    sample_document: Document,
) -> None:
    with pytest.raises(
        ValueError,
        match="Tag cannot be empty",
    ):
        sample_document.add_tag("   ")


def test_document_rejects_blank_title() -> None:
    with pytest.raises(
        ValueError,
        match="Title cannot be empty",
    ):
        Document(
            document_id=1,
            title="   ",
            content="Treść.",
        )


def test_document_rejects_blank_content() -> None:
    with pytest.raises(
        ValueError,
        match="Content cannot be empty",
    ):
        Document(
            document_id=1,
            title="Tytuł",
            content="   ",
        )

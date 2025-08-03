"""Basic tests to ensure pytest runs successfully."""


def test_basic_arithmetic():
    """Test basic arithmetic operations."""
    assert 2 + 2 == 4
    assert 10 - 5 == 5
    assert 3 * 4 == 12


def test_string_operations():
    """Test basic string operations."""
    text = "Hello, World!"
    assert text.lower() == "hello, world!"
    assert len(text) == 13
    assert "World" in text


def test_list_operations():
    """Test basic list operations."""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert sum(numbers) == 15
    assert max(numbers) == 5
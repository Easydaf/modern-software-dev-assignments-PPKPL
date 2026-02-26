import pytest
from unittest.mock import patch, MagicMock

from ..app.services.extract import extract_action_items, extract_action_items_llm


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_bullet_list(mock_chat: MagicMock):
    """Bullet list input returns extracted items from mocked LLM response."""
    mock_chat.return_value = {
        "message": {"content": '["Set up database", "Implement API", "Write tests"]'}
    }
    text = """
    Notes from meeting:
    - Set up database
    * Implement API
    1. Write tests
    """
    result = extract_action_items_llm(text)
    assert result == ["Set up database", "Implement API", "Write tests"]
    mock_chat.assert_called_once()
    call_args = mock_chat.call_args
    assert call_args.kwargs["model"] == "llama3.1:8b"
    assert "Set up database" in call_args.kwargs["messages"][0]["content"]


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_keyword_prefixed(mock_chat: MagicMock):
    """Keyword-prefixed lines input returns extracted items from mocked LLM response."""
    mock_chat.return_value = {
        "message": {"content": '["Review pull request", "Update documentation"]'}
    }
    text = """
    todo: Review pull request
    action: Update documentation
    next: Deploy to staging
    """
    result = extract_action_items_llm(text)
    assert result == ["Review pull request", "Update documentation"]
    mock_chat.assert_called_once()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_empty_input(mock_chat: MagicMock):
    """Empty input returns empty list from mocked LLM response."""
    mock_chat.return_value = {"message": {"content": "[]"}}
    result = extract_action_items_llm("")
    assert result == []
    mock_chat.assert_called_once()


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_json_with_markdown(mock_chat: MagicMock):
    """LLM response wrapped in markdown code block is parsed correctly."""
    mock_chat.return_value = {
        "message": {
            "content": '```json\n["Task one", "Task two"]\n```'
        }
    }
    result = extract_action_items_llm("Some text")
    assert result == ["Task one", "Task two"]


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_invalid_json_returns_empty(mock_chat: MagicMock):
    """Invalid JSON in LLM response returns empty list."""
    mock_chat.return_value = {
        "message": {"content": "Here are the items: 1. Do X 2. Do Y"}
    }
    result = extract_action_items_llm("Some text")
    assert result == []


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items

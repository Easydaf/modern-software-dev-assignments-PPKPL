from backend.app.services.extract import extract_action_items


def test_extract_action_items():
    text = """
    This is a note
    - TODO: write tests
    - ACTION: review PR
    - TASK: update docs
    - BUG: fix crash on startup
    - FIXME: remove hardcoded value
    - [ ] Ship release notes
    - [x] Prepare changelog
    - @alice please review this
    Not actionable sentence.
    """.strip()

    items = extract_action_items(text)
    assert "TODO: write tests" in items
    assert "ACTION: review PR" in items
    assert "TASK: update docs" in items
    assert "BUG: fix crash on startup" in items
    assert "FIXME: remove hardcoded value" in items
    assert "[ ] Ship release notes" in items
    assert "[x] Prepare changelog" in items
    assert "@alice please review this" in items
    assert "This is a note" not in items
    assert "Not actionable sentence." not in items


def test_extract_action_items_advanced_patterns():
    text = """
    This should not be extracted.
    - [ ] Follow up with client
    - [x] Publish changelog
    - TASK: refactor extraction module
    - BUG: fix pagination edge case
    - FIXME: remove temporary workaround
    - @bob check deployment logs
    We discussed timelines in the meeting.
    """.strip()

    items = extract_action_items(text)

    assert "[ ] Follow up with client" in items
    assert "[x] Publish changelog" in items
    assert "TASK: refactor extraction module" in items
    assert "BUG: fix pagination edge case" in items
    assert "FIXME: remove temporary workaround" in items
    assert "@bob check deployment logs" in items
    assert "This should not be extracted." not in items
    assert "We discussed timelines in the meeting." not in items

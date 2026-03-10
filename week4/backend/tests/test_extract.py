from backend.app.services.extract import extract_action_items, extract_tags


def test_extract_action_items():
    text = """
    This is a note
    - TODO: write tests
    - Ship it!
    Not actionable
    """.strip()
    items = extract_action_items(text)
    assert "TODO: write tests" in items
    assert "Ship it!" in items


def test_extract_tags():
    text = "Catatan #ide untuk sprint ini, jangan lupa tandai #penting sebelum rilis."
    tags = extract_tags(text)
    assert len(tags) == 2
    assert "#ide" in tags
    assert "#penting" in tags

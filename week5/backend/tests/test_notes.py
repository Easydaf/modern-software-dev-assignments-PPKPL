def test_create_and_list_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    body = r.json()
    assert body["ok"] is True
    assert body["data"]["title"] == "Test"

    r = client.get("/notes/")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    data = body["data"]
    assert "items" in data
    assert "total" in data
    assert data["total"] >= 1
    assert len(data["items"]) >= 1

    r = client.get("/notes/search/")
    assert r.status_code == 200
    assert r.json()["ok"] is True

    r = client.get("/notes/search/", params={"q": "Hello"})
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert len(body["data"]) >= 1


def test_notes_pagination(client):
    """Test page/page_size params and boundary cases."""
    for i in range(5):
        client.post("/notes/", json={"title": f"N{i}", "content": f"C{i}"})

    # page_size smaller than total
    r = client.get("/notes/", params={"page": 1, "page_size": 2})
    body = r.json()["data"]
    assert len(body["items"]) == 2
    assert body["total"] >= 5

    # second page
    r = client.get("/notes/", params={"page": 2, "page_size": 2})
    body = r.json()["data"]
    assert len(body["items"]) == 2

    # empty last page (page beyond data)
    r = client.get("/notes/", params={"page": 999, "page_size": 10})
    body = r.json()["data"]
    assert body["items"] == []
    assert body["total"] >= 5

    # large page_size returns all items in one page
    r = client.get("/notes/", params={"page": 1, "page_size": 100})
    body = r.json()["data"]
    assert len(body["items"]) == body["total"]


def test_get_note_not_found(client):
    """GET /notes/{id} with non-existent id returns error envelope."""
    r = client.get("/notes/9999")
    assert r.status_code == 404
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "NOT_FOUND"
    assert "message" in body["error"]


def test_create_note_validation_error(client):
    """POST /notes/ with empty title returns validation error envelope."""
    r = client.post("/notes/", json={"title": "", "content": "x"})
    assert r.status_code == 422
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "VALIDATION_ERROR"
    assert "message" in body["error"]

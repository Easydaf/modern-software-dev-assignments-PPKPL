def test_create_and_complete_action_item(client):
    payload = {"description": "Ship it"}
    r = client.post("/action-items/", json=payload)
    assert r.status_code == 201, r.text
    body = r.json()
    assert body["ok"] is True
    item = body["data"]
    assert item["completed"] is False

    r = client.put(f"/action-items/{item['id']}/complete")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    assert body["data"]["completed"] is True

    r = client.get("/action-items/")
    assert r.status_code == 200
    body = r.json()
    assert body["ok"] is True
    data = body["data"]
    assert "items" in data
    assert "total" in data
    assert data["total"] == 1
    assert len(data["items"]) == 1


def test_action_items_pagination(client):
    """Test page/page_size params and boundary cases."""
    for i in range(5):
        client.post("/action-items/", json={"description": f"Task {i}"})

    # page_size smaller than total
    r = client.get("/action-items/", params={"page": 1, "page_size": 2})
    body = r.json()["data"]
    assert len(body["items"]) == 2
    assert body["total"] >= 5

    # second page
    r = client.get("/action-items/", params={"page": 2, "page_size": 2})
    body = r.json()["data"]
    assert len(body["items"]) == 2

    # empty last page (page beyond data)
    r = client.get("/action-items/", params={"page": 999, "page_size": 10})
    body = r.json()["data"]
    assert body["items"] == []
    assert body["total"] >= 5

    # large page_size returns all items in one page
    r = client.get("/action-items/", params={"page": 1, "page_size": 100})
    body = r.json()["data"]
    assert len(body["items"]) == body["total"]


def test_complete_item_not_found(client):
    """PUT /action-items/{id}/complete with non-existent id returns error envelope."""
    r = client.put("/action-items/9999/complete")
    assert r.status_code == 404
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "NOT_FOUND"
    assert "message" in body["error"]


def test_create_item_validation_error(client):
    """POST /action-items/ with empty description returns validation error envelope."""
    r = client.post("/action-items/", json={"description": ""})
    assert r.status_code == 422
    body = r.json()
    assert body["ok"] is False
    assert body["error"]["code"] == "VALIDATION_ERROR"
    assert "message" in body["error"]

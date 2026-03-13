def test_create_list_and_patch_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"
    assert "created_at" in data and "updated_at" in data

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/", params={"q": "Hello", "limit": 10, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    note_id = data["id"]
    r = client.patch(f"/notes/{note_id}", json={"title": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["title"] == "Updated"


def test_notes_pagination_and_sorting(client):
    # Create 5 notes in order so IDs and creation times are sequential
    titles = [f"Pagination Note {i}" for i in range(1, 6)]
    created_ids: list[int] = []
    for title in titles:
        r = client.post("/notes/", json={"title": title, "content": f"Content for {title}"})
        assert r.status_code == 201
        created_ids.append(r.json()["id"])

    # --- Pagination ---
    # Page 1: first 3 records sorted by ascending id
    r = client.get("/notes/", params={"skip": 0, "limit": 3, "sort": "id"})
    assert r.status_code == 200
    page1 = r.json()
    assert len(page1) == 3

    # Page 2: next records starting at offset 3 (only 2 remain)
    r = client.get("/notes/", params={"skip": 3, "limit": 3, "sort": "id"})
    assert r.status_code == 200
    page2 = r.json()
    assert len(page2) == 2

    # Pages must not overlap and together cover all 5 created notes
    page1_ids = {n["id"] for n in page1}
    page2_ids = {n["id"] for n in page2}
    assert page1_ids.isdisjoint(page2_ids), "Pages must not contain duplicate notes"
    assert page1_ids | page2_ids == set(created_ids), "Both pages together must cover all created notes"

    # limit=0 should return an empty list
    r = client.get("/notes/", params={"skip": 0, "limit": 0, "sort": "id"})
    assert r.status_code == 200
    assert r.json() == []

    # skip beyond total count should return an empty list
    r = client.get("/notes/", params={"skip": 100, "limit": 10, "sort": "id"})
    assert r.status_code == 200
    assert r.json() == []

    # --- Sorting ---
    # Ascending by id: ids must be in increasing order
    r = client.get("/notes/", params={"sort": "id", "limit": 10})
    assert r.status_code == 200
    asc_ids = [n["id"] for n in r.json()]
    assert asc_ids == sorted(asc_ids), "sort=id must return notes in ascending id order"

    # Descending by id: ids must be in decreasing order
    r = client.get("/notes/", params={"sort": "-id", "limit": 10})
    assert r.status_code == 200
    desc_ids = [n["id"] for n in r.json()]
    assert desc_ids == sorted(desc_ids, reverse=True), "sort=-id must return notes in descending id order"

    # Default sort is -created_at (newest first): the last-created note must appear first
    r = client.get("/notes/", params={"limit": 10})
    assert r.status_code == 200
    default_items = r.json()
    default_ids = [n["id"] for n in default_items]
    assert default_ids[0] == created_ids[-1], "Default sort (-created_at) must return newest note first"
    assert default_ids[-1] == created_ids[0], "Default sort (-created_at) must return oldest note last"

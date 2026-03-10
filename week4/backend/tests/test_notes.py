def test_create_and_list_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/search/")
    assert r.status_code == 200

    r = client.get("/notes/search/", params={"q": "Hello"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1


def test_update_note(client):
    # Buat catatan baru dulu
    payload = {"title": "Judul Lama", "content": "Konten Lama"}
    r = client.post("/notes/", json=payload)
    note_id = r.json()["id"]

    # Tes Edit (PUT)
    update_payload = {"title": "Judul Baru", "content": "Konten Baru"}
    r = client.put(f"/notes/{note_id}", json=update_payload)
    assert r.status_code == 200
    assert r.json()["title"] == "Judul Baru"


def test_delete_note(client):
    # Buat catatan baru dulu
    payload = {"title": "Hapus Saya", "content": "Konten"}
    r = client.post("/notes/", json=payload)
    note_id = r.json()["id"]

    # Tes Hapus (DELETE)
    r = client.delete(f"/notes/{note_id}")
    assert r.status_code == 204

    # Verifikasi catatan benar-benar hilang (Harus dapat 404 Not Found)
    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 404


def test_create_note_validation_error(client):
    # Tes mengirim catatan dengan title kosong
    payload = {"title": "", "content": "Konten valid"}
    r = client.post("/notes/", json=payload)

    # Harus ditolak oleh FastAPI (status 422 Unprocessable Entity)
    assert r.status_code == 422
    data = r.json()
    # Memastikan error-nya benar-benar dari validasi title
    assert data["detail"][0]["loc"][-1] == "title"

from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Note
from ..schemas import NoteCreate, NoteRead, PaginatedNoteResponse

router = APIRouter(prefix="/notes", tags=["notes"])


def _ok(data: Any) -> dict:
    return {"ok": True, "data": data}


@router.get("/")
def list_notes(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
) -> dict:
    total = db.execute(select(func.count(Note.id))).scalar()
    offset = (page - 1) * page_size
    rows = db.execute(select(Note).offset(offset).limit(page_size)).scalars().all()
    payload = PaginatedNoteResponse(
        items=[NoteRead.model_validate(row) for row in rows],
        total=total,
    )
    return _ok(payload.model_dump())


@router.post("/", status_code=201)
def create_note(payload: NoteCreate, db: Session = Depends(get_db)) -> dict:
    note = Note(title=payload.title, content=payload.content)
    db.add(note)
    db.flush()
    db.refresh(note)
    return _ok(NoteRead.model_validate(note).model_dump())


@router.get("/search/")
def search_notes(q: Optional[str] = None, db: Session = Depends(get_db)) -> dict:
    if not q:
        rows = db.execute(select(Note)).scalars().all()
    else:
        rows = (
            db.execute(select(Note).where((Note.title.contains(q)) | (Note.content.contains(q))))
            .scalars()
            .all()
        )
    return _ok([NoteRead.model_validate(row).model_dump() for row in rows])


@router.get("/{note_id}")
def get_note(note_id: int, db: Session = Depends(get_db)) -> dict:
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return _ok(NoteRead.model_validate(note).model_dump())

from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import ActionItem
from ..schemas import ActionItemCreate, ActionItemRead, PaginatedActionItemResponse

router = APIRouter(prefix="/action-items", tags=["action_items"])


def _ok(data: Any) -> dict:
    return {"ok": True, "data": data}


@router.get("/")
def list_items(
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
) -> dict:
    total = db.execute(select(func.count(ActionItem.id))).scalar()
    offset = (page - 1) * page_size
    rows = db.execute(select(ActionItem).offset(offset).limit(page_size)).scalars().all()
    payload = PaginatedActionItemResponse(
        items=[ActionItemRead.model_validate(row) for row in rows],
        total=total,
    )
    return _ok(payload.model_dump())


@router.post("/", status_code=201)
def create_item(payload: ActionItemCreate, db: Session = Depends(get_db)) -> dict:
    item = ActionItem(description=payload.description, completed=False)
    db.add(item)
    db.flush()
    db.refresh(item)
    return _ok(ActionItemRead.model_validate(item).model_dump())


@router.put("/{item_id}/complete")
def complete_item(item_id: int, db: Session = Depends(get_db)) -> dict:
    item = db.get(ActionItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Action item not found")
    item.completed = True
    db.add(item)
    db.flush()
    db.refresh(item)
    return _ok(ActionItemRead.model_validate(item).model_dump())

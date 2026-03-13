from typing import Any

from pydantic import BaseModel, Field

# --------------- Envelope models ---------------


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorEnvelope(BaseModel):
    ok: bool = False
    error: ErrorDetail


class SuccessEnvelope(BaseModel):
    ok: bool = True
    data: Any = None


# --------------- Note schemas ---------------


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)


class NoteRead(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True


class PaginatedNoteResponse(BaseModel):
    items: list[NoteRead]
    total: int


# --------------- Action item schemas ---------------


class ActionItemCreate(BaseModel):
    description: str = Field(..., min_length=1)


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool

    class Config:
        from_attributes = True


class PaginatedActionItemResponse(BaseModel):
    items: list[ActionItemRead]
    total: int

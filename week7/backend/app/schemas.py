from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field, field_validator

NonEmptyText = Annotated[str, Field(min_length=1, pattern=r".*\S.*")]
TitleText = Annotated[
    str,
    Field(min_length=1, max_length=200, pattern=r".*\S.*"),
]


class NoteCreate(BaseModel):
    title: TitleText
    content: NonEmptyText

    @field_validator("title", "content")
    @classmethod
    def strip_text_fields(cls, value: str) -> str:
        return value.strip()


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NotePatch(BaseModel):
    title: TitleText | None = None
    content: NonEmptyText | None = None

    @field_validator("title", "content")
    @classmethod
    def strip_text_fields(cls, value: str | None) -> str | None:
        if value is None:
            return None
        return value.strip()


class ActionItemCreate(BaseModel):
    description: NonEmptyText

    @field_validator("description")
    @classmethod
    def strip_description(cls, value: str) -> str:
        return value.strip()


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ActionItemPatch(BaseModel):
    description: NonEmptyText | None = None
    completed: bool | None = None

    @field_validator("description")
    @classmethod
    def strip_description(cls, value: str | None) -> str | None:
        if value is None:
            return None
        return value.strip()

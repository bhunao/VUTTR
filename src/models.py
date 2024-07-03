from datetime import date
from typing import Optional

from sqlmodel import Field, Relationship

from src.core.database import MODEL


class ExampleModelSchema(MODEL):
    name: str
    favorite_number: int
    date: date


class ExampleModel(MODEL, table=True):
    __tablename__ = "example_model"

    id: Optional[int] = Field(nullable=False, primary_key=True)
    name: str
    favorite_number: int
    date: date


class ToolSchema(MODEL):
    __tablename__ = "tools"

    title: str
    link: str
    description: str
    # tags: list[str]


class Tool(ToolSchema, table=True):
    __tablename__ = "tools"

    id: Optional[int] = Field(nullable=False, primary_key=True)
    # tags: list["Tag"] = Relationship(
    #     back_populates="tools", link_model="ToolTagLink")


class Tag(MODEL, table=True):
    __tablename__ = "tags"

    id: Optional[int] = Field(nullable=False, primary_key=True)
    name: str


# class ToolTagLink(MODEL, table=True):
#     tool_id: Optional[int] = Field(
#         default=None, foreign_key="tools.id", primary_key=True)
#     tag_id: Optional[int] = Field(
#         default=None, foreign_key="tags.id", primary_key=True)

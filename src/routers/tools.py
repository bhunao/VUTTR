from typing import Optional

from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.database import Database
from src.models import Tool, ToolSchema
from src.core.dependencies import get_session
from src.core.errors import HTTP404_ITEM_NOT_FOUND

router = APIRouter(
    prefix="/tools"
)

DependSession = Depends(get_session)


@router.get("/")
async def get_tools(session: Session = DependSession, tag: Optional[str] = None):
    db = Database(session)
    tools = db.read_all(Tool)
    return tools


@router.post("/")
async def create_tool(record: ToolSchema, session: Session = DependSession):
    db = Database(session)
    new_record = db.create(record, Tool)
    return new_record


@router.delete("/")
async def delete_tool(id: int, session: Session = DependSession):
    db = Database(session)
    deleted = db.delete(Tool, id)
    if not deleted:
        raise HTTP404_ITEM_NOT_FOUND
    return {}

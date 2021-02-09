from typing import Any

import app.crud
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/tx/{hash}")
def get_events_by_tx(*, hash: str, skip: int = 0, limit: int = 0) -> Any:
    """
    Get event by transaction
    """
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip parameter invalid")
    if limit < 0:
        raise HTTPException(status_code=400, detail="limit parameter invalid")

    events = crud.event.get_by_tx(hash, skip, limit)
    if len(events) == 0:
        raise HTTPException(status_code=404, detail="Events not found")
    return events


@router.get("/block")
def get_events_latest_block(skip: int = 0, limit: int = 0) -> Any:
    """
    Get events in latest block
    """
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip parameter invalid")
    if limit < 0:
        raise HTTPException(status_code=400, detail="limit parameter invalid")

    events = crud.event.get_by_latest_block(skip, limit)
    if len(events) == 0:
        raise HTTPException(status_code=404, detail="Events not found")
    return events


@router.get("/block/{height}")
def get_events_by_height(*, height: int, skip: int = 0, limit: int = 0) -> Any:
    """
    Get events by block height
    """
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip parameter invalid")
    if limit < 0:
        raise HTTPException(status_code=400, detail="limit parameter invalid")

    events = crud.event.get_by_block(height, skip, limit)
    if len(events) == 0:
        raise HTTPException(status_code=404, detail="Events not found")
    return events

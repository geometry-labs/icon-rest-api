from typing import Any

from app import crud
from fastapi import APIRouter, HTTPException, WebSocket

router = APIRouter()


@router.get("/")
def get_block_latest(skip: int = 0, limit: int = 1) -> Any:
    """
    Get latest block
    """
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip parameter invalid")
    if limit < 0:
        raise HTTPException(status_code=400, detail="limit parameter invalid")

    blocks = crud.block.get_latest_blocks(skip, limit)
    if len(blocks) == 0:
        raise HTTPException(status_code=404, detail="Block not found")
    return blocks


@router.get("/height/{height}")
def get_block_by_height(
    *,
    height: int,
) -> Any:
    """
    Get block by height.
    """
    block = crud.block.get_by_height(height)
    if not block:
        raise HTTPException(status_code=404, detail="Block not found")
    return block


@router.get("/hash/{hash}")
def get_block_by_hash(
    *,
    hash: str,
) -> Any:
    """
    Get block by hash.
    """
    block = crud.block.get_by_hash(hash)
    if not block:
        raise HTTPException(status_code=404, detail="Block not found")
    return block

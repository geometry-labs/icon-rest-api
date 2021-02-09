from typing import Any

import app.crud
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/hash/{hash}")
def get_tx_by_hash(*, hash: str) -> Any:
    """
    Get transaction by hash
    """
    tx = crud.transaction.get_by_hash(hash)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx


@router.get("/address/{address}")
def get_txs_by_address(*, address: str, skip: int = 0, limit: int = 0) -> Any:
    """
    Get transaction by address
    """
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip parameter invalid")
    if limit < 0:
        raise HTTPException(status_code=400, detail="limit parameter invalid")

    txs = crud.transaction.get_by_address(address, skip, limit)
    if len(txs) == 0:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return txs


@router.get("/block")
def get_txs_latest_block(skip: int = 0, limit: int = 0) -> Any:
    """
    Get transactions in latest block
    """
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip parameter invalid")
    if limit < 0:
        raise HTTPException(status_code=400, detail="limit parameter invalid")

    txs = crud.transaction.get_by_latest_block(skip, limit)
    if len(txs) == 0:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return txs


@router.get("/block/{height}")
def get_txs_by_height(*, height: int, skip: int = 0, limit: int = 0) -> Any:
    """
    Get transactions by block height
    """
    if skip < 0:
        raise HTTPException(status_code=400, detail="skip parameter invalid")
    if limit < 0:
        raise HTTPException(status_code=400, detail="limit parameter invalid")

    txs = crud.transaction.get_by_block(height, skip, limit)
    if len(txs) == 0:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return txs

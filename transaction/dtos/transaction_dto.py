# dtos/transaction_dto.py
from pydantic import BaseModel, Field
from typing import Optional


class TransactionDTO(BaseModel):
    id: int = Field(..., gt=0, description="Id of Transction, should be greater than 0")
    amount: float = Field(..., gt=0, description="Transaction amount should be greater than zero.")
    type: str = Field(..., min_length=1, description="Transaction type cannot be empty.")
    parent_id: Optional[int] = Field(None, description="Parent ID is optional and must be an integer if provided.")


class TransactionResponseDTO(BaseModel):
    id: int
    amount: float
    type: str
    parent_id: Optional[int]

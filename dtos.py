
from pydantic import BaseModel

class TransactionDTO(BaseModel):
    transaction_id: int
    amount: float
    currency: str

class ConversionDTO(BaseModel):
    from_currency: str
    to_currency: str
    amount: float

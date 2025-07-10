from pydantic import BaseModel
from decimal import Decimal

class WalletOut(BaseModel):
    identifier: str
    balance: Decimal
    currency: str

    class Config:
        orm_mode = True

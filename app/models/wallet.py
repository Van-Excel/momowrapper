import uuid
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID

class Wallet(Base):
    __tablename__ = "wallets"
    __table_args__ = (
        UniqueConstraint('user_id', name='unique_user_wallet'),
    )

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(UUID(as_uuid=True), unique=True, index=True,  default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    balance = Column(Numeric(precision=12, scale=2), default=0.00)
    currency = Column(String(3), default="GHS")

    # Optional: backref
    user = relationship("User", backref="wallet")

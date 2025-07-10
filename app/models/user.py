import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Integer
from app.db.base import Base
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, index=True)

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

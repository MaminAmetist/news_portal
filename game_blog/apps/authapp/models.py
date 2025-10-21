from sqlalchemy import Boolean, Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, UUIDType
from uuid import uuid4
import datetime

from db.base_class import Base


class User(Base):
    user_id = Column(UUIDType, primary_key=True, default=uuid4)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    email = Column(EmailType)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    post = relationship("Post", back_populates="owner")
    token = Column(String(64), nullable=True)

from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
import datetime

from db.base_class import Base


class Post(Base):
    post_id = Column(UUIDType, primary_key=True, default=uuid4)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("user.user_id"))
    owner = relationship("User", back_populates="post")

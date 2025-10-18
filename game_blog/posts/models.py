from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

from sqlalchemy_utils import UUIDType

from ..database import Base


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(UUIDType, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.user_id"))
    owner = relationship("User", back_populates="post")

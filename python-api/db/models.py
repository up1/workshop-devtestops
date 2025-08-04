from sqlalchemy import TIMESTAMP, Column, Integer, String, text

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
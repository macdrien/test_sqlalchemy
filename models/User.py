from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    teams = relationship('Team', secondary='member')

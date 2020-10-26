from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    members = relationship('User', secondary='member')

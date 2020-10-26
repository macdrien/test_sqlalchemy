from sqlalchemy import Column, Integer, String, ForeignKey
from models import Base


class Member(Base):
    __tablename__ = 'member'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)

from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Users(Base):
    __tablename__ = 'LoginUsers'

    UserId = Column(String, primary_key=True)
    UserName = Column(String)
    Email = Column(String)
    Password = Column(String)
    IsDeleted =Column(Integer)
    IsActive =Column(Integer)
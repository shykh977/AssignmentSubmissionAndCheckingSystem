from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Society(Base):
    __tablename__ = 'SocityName'

    SocityId = Column(String, primary_key=True)
    SocityName = Column(String)
    UserId = Column(String)


    

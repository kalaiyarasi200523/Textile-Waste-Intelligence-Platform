from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    waste_batch_id = Column(String)
    fabric_type = Column(String)
    source = Column(String)
    quantity = Column(String)
    color = Column(String)
    condition = Column(String)
    collection_date = Column(String)

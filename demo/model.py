from sqlalchemy import Column, Integer, String, Text, DateTime
from db import Base, engine
from pydantic import BaseModel
from datetime import datetime

class ToDoTable(Base):
    __tablename__ = 'todo_list'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text, nullable=False)
    contents = Column(Text, nullable=False)
    date = Column(Text, nullable=False)

class ToDo(BaseModel):
    id: int
    title: str
    contents: str
    date: str
    
def main():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    main()
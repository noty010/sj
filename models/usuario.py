from sqlalchemy import Column, Integer, String, Boolean
from .base import BaseModel

class Usuario(BaseModel):
    __tablename__ = 'usuario'
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    isadmin = Column(Boolean, nullable=False, default=False)
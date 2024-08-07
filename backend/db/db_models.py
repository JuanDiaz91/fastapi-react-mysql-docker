import bcrypt
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), index=True, unique=True, nullable=False)
    email = Column(String(50), index=True, unique=True, nullable=False)
    password = Column(String(200), index=True, nullable=False)
    tasks = relationship('Task', back_populates='owner')

    def verify_password(self, plain_password: str):
        verify_password = bcrypt.checkpw(plain_password.encode('utf-8'), self.password.encode('utf-8'))

        return verify_password


class Task(Base):
    __tablename__= 'task'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    owner = relationship('User', back_populates='tasks')

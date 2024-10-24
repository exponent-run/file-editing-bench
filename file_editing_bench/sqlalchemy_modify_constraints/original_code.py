from sqlalchemy import Column, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(255))
    department = Column(String(100))
    hire_date = Column(DateTime, default=datetime.utcnow)
    salary = Column(Integer)
    
    def __repr__(self):
        return f"<Employee {self.first_name} {self.last_name}>"

# Simple index
employees_email_idx = Table(
    'employees', Base.metadata,
    Column('email', String(255))
)
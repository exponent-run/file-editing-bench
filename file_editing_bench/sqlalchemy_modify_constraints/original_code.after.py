from sqlalchemy import Column, Integer, String, DateTime, Table, CheckConstraint, UniqueConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), nullable=False)
    department = Column(String(100), nullable=False)
    hire_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    salary = Column(Integer, nullable=False)
    
    # Add check constraint for salary
    __table_args__ = (
        CheckConstraint('salary >= 30000', name='check_min_salary'),
        CheckConstraint('salary <= 500000', name='check_max_salary'),
        UniqueConstraint('email', name='uq_employee_email'),
        Index('idx_employee_dept_hire', 'department', 'hire_date'),
        {'extend_existing': True}
    )
    
    def __repr__(self):
        return f"<Employee {self.first_name} {self.last_name}>"

# Remove the simple index since we're using __table_args__
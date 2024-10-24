from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    order_number = Column(String(50), unique=True, nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    shipping_address = Column(String(500), nullable=False)
    status = Column(String(20), nullable=False, default='pending')
    
    def __repr__(self):
        return f"<Order {self.order_number}>"
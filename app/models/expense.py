from sqlalchemy import Column, Integer, Float, String
from app.database.session import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)

    merchant = Column(String)
    amount = Column(Float)

    category = Column(String)
    status = Column(String)

    receipt_path = Column(String)
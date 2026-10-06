from sqlalchemy import Column, Integer, String
from app.database.session import Base


class Approval(Base):
    __tablename__ = "approvals"

    id = Column(Integer, primary_key=True, index=True)

    expense_id = Column(Integer)

    approver = Column(String)

    status = Column(String)

    remarks = Column(String)
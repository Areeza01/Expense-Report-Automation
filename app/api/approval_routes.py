from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.expense import Expense

router = APIRouter(
    prefix="/approvals",
    tags=["Approvals"]
)


@router.put("/{expense_id}/approve")
def approve_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    expense.status = "Approved"

    db.commit()

    return {"message": "Approved"}


@router.put("/{expense_id}/reject")
def reject_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    expense.status = "Rejected"

    db.commit()

    return {"message": "Rejected"}
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.expense import Expense

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db)
):

    expenses = db.query(
        Expense
    ).all()

    total_expenses = len(expenses)

    total_amount = sum(
        expense.amount
        for expense in expenses
    )

    pending = len([
        expense
        for expense in expenses
        if expense.status == "Pending"
    ])

    approved = len([
        expense
        for expense in expenses
        if expense.status == "Approved"
    ])

    rejected = len([
        expense
        for expense in expenses
        if expense.status == "Rejected"
    ])

    return {
        "total_expenses": total_expenses,
        "total_amount": total_amount,
        "pending": pending,
        "approved": approved,
        "rejected": rejected
    }
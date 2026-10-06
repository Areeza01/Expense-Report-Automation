from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.expense import Expense
from app.repositories.expense_repository import (
    ExpenseRepository
)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.get("/")
def get_expenses(
    db: Session = Depends(get_db)
):
    return ExpenseRepository.get_all(db)


@router.post("/")
def create_expense(
    expense_data: dict,
    db: Session = Depends(get_db)
):

    expense = Expense(
        employee_id=expense_data["employee_id"],
        merchant=expense_data["merchant"],
        amount=expense_data["amount"],
        category=expense_data["category"],
        status="Pending"
    )

    return ExpenseRepository.create(
        db,
        expense
    )


@router.put("/{expense_id}/approve")
def approve_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id)
        .first()
    )

    if not expense:
        return {
            "error": "Expense not found"
        }

    expense.status = "Approved"

    db.commit()
    db.refresh(expense)

    return expense


@router.put("/{expense_id}/reject")
def reject_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id)
        .first()
    )

    if not expense:
        return {
            "error": "Expense not found"
        }

    expense.status = "Rejected"

    db.commit()
    db.refresh(expense)

    return expense
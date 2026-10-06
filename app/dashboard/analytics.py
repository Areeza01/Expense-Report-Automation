from sqlalchemy import func
from app.models.expense import Expense


def dashboard_stats(db):

    total_expenses = db.query(
        func.count(Expense.id)
    ).scalar()

    total_amount = db.query(
        func.sum(Expense.amount)
    ).scalar()

    return {
        "total_expenses": total_expenses or 0,
        "total_amount": total_amount or 0
    }
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.expense import Expense


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/")
def get_reports(
    db: Session = Depends(get_db)
):

    expenses = (
        db.query(Expense)
        .all()
    )

    return {
        "total_records": len(expenses),
        "expenses": expenses
    }

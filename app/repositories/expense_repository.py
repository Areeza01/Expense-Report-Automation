from app.models.expense import Expense


class ExpenseRepository:

    @staticmethod
    def create(db, expense):

        db.add(expense)
        db.commit()
        db.refresh(expense)

        return expense

    @staticmethod
    def get_all(db):

        return db.query(Expense).all()

    @staticmethod
    def get_by_id(db, expense_id):

        return (
            db.query(Expense)
            .filter(
                Expense.id == expense_id
            )
            .first()
        )
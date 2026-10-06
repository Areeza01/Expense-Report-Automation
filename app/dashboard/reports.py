from app.models.expense import Expense


def expense_report(db):

    expenses = db.query(
        Expense
    ).all()

    report = []

    for expense in expenses:
        report.append({
            "merchant": expense.merchant,
            "amount": expense.amount,
            "category": expense.category,
            "status": expense.status
        })

    return report
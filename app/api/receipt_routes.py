import os
import shutil
import json

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.vision_service import VisionService
from app.services.categorization_service import CategorizationService
from app.services.validation_service import ValidationService
from app.services.approval_service import ApprovalService

from app.models.expense import Expense
from app.repositories.expense_repository import ExpenseRepository


router = APIRouter(
    prefix="/receipts",
    tags=["Receipts"]
)

vision_service = VisionService()
categorization_service = CategorizationService()
approval_service = ApprovalService()


@router.post("/upload")
async def upload_receipt(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    upload_dir = "uploads/receipts"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    # STEP 1
    receipt_data = vision_service.extract_receipt(
        file_path
    )

    merchant = receipt_data.get(
        "merchant_name",
        "Unknown"
    )

    amount = float(
        receipt_data.get(
            "total_amount",
            0
        )
    )

    # STEP 2
    category_response = (
        categorization_service.categorize(
            merchant,
            amount
        )
    )

    if isinstance(category_response, str):
        try:
            category_response = json.loads(
                category_response
            )
        except:
            category_response = {
                "category": "Other"
            }

    category = category_response.get(
        "category",
        "Other"
    )

    # STEP 3
    validation_result = (
        ValidationService.validate(
            category,
            amount
        )
    )

    # STEP 4
    approval_response = (
        approval_service.evaluate(
            merchant,
            amount,
            category,
            validation_result
        )
    )

    # STEP 5
    expense = Expense(
        employee_id=1,
        merchant=merchant,
        amount=amount,
        category=category,
        status="Pending",
        receipt_path=file_path
    )

    saved_expense = (
        ExpenseRepository.create(
            db,
            expense
        )
    )

    return {
        "expense_id": saved_expense.id,
        "receipt_data": receipt_data,
        "category": category_response,
        "validation": validation_result,
        "approval": approval_response
    }
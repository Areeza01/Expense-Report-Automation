from fastapi import FastAPI

from app.database.session import Base
from app.database.db import engine

from app.api.expense_routes import router as expense_router
from app.api.approval_routes import router as approval_router
from app.api.receipt_routes import router as receipt_router
from app.api.dashboard_routes import router as dashboard_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Report Automation"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(expense_router)
app.include_router(approval_router)
app.include_router(receipt_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {
        "message": "Expense Report Automation API Running"
    }
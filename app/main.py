from fastapi import FastAPI
from .database import Base, engine
from .routers import users, expenses

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ExpenseTracker",
    description="API для учёта расходов",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(expenses.router)

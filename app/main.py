from fastapi import FastAPI
from app.routers import users, expenses

app = FastAPI()

app.include_router(users.router)
app.include_router(expenses.router)

from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel
from app.database import engine
from app.routers import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs when the app starts up. We create the database tables.
    SQLModel.metadata.create_all(engine)
    yield
    # This runs when the app shuts down.

app = FastAPI(title="Learning FastAPI", lifespan=lifespan)

# Include the users router
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to your FastAPI Learning App!"}

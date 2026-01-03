from fastapi import FastAPI
from models import Base
from database import engine
from routers import auth, todos

app = FastAPI(title="FastAPI Vercel App")

# Create tables (use Alembic for production migrations)
Base.metadata.create_all(bind=engine, checkfirst=True)

# Include routers with prefixes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(todos.router, prefix="/todo", tags=["todos"])

# Root endpoint for testing
@app.get("/")
async def root():
    return {"message": "FastAPI app is running!"}

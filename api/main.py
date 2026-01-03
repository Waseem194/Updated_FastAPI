
from fastapi import FastAPI
from models import Base
from database import engine
from routers import auth, todos

app = FastAPI()

Base.metadata.create_all(bind=engine,checkfirst=True)


app.include_router(todos.router)
app.include_router(auth.router)
    
 
       



    


    
from typing import Annotated
from fastapi import APIRouter,Depends, HTTPException, Path,status
from sqlalchemy.orm import Session
from models import Todos,Base
from database import SessionLocal, engine
from schemas import TodoRequest



router = APIRouter(
    prefix='/todo',
    tags=['todo']
)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]


        
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(db:db_dependency):
    
    return db.query(Todos).all()
    
    
@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def get_single_todo(db:db_dependency,
                                    todo_id:int = Path(gt=0)):
    

    get_todo_by_id = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if get_todo_by_id is not None:
        return get_todo_by_id
    raise HTTPException(status_code=404,detail='todo not found!')  
       

@router.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,
                            todo_request:TodoRequest):

    
    todo_items = Todos(**todo_request.model_dump())
    db.add(todo_items)
    db.commit()
    db.refresh(todo_items)
    return todo_items
 
    
@router.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency,
                            todo_request:TodoRequest,todo_id:int=Path(gt=0)):
    
    
    
    update_todo_item = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if update_todo_item is  None:
        raise HTTPException(status_code=404,detail='Todo is Not Found!')
    
    update_todo_item.title = todo_request.title
    update_todo_item.description = todo_request.description
    update_todo_item.priority = todo_request.priority
    update_todo_item.complete = todo_request.complete
    
    db.add(update_todo_item)
    db.commit()
    # db.refresh(update_todo_item)
    # return update_todo_item


@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int = Path(gt=0)):
    
    
    
    delete_todo_item = db.query(Todos).filter(Todos.id == todo_id).first()
    if delete_todo_item is None:
        raise HTTPException(status_code=404,detail='todo is Not Found!')
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
    
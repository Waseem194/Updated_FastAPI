from pydantic import BaseModel,Field


class TodoRequest(BaseModel):
    title:str = Field(min_length=1)
    description:str = Field(min_length=1,max_length=100)
    priority:int = Field(gt=0,lt=6)
    complete:bool

class UserRequest(BaseModel):
    first_name:str
    last_name:str
    username:str
    email:str
    password:str
    role:str
    
class Token(BaseModel):
    access_token:str
    token_type:str
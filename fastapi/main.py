from typing import List, Optional
from pydantic import BaseModel, Field
from enum import IntEnum
from fastapi import FastAPI, HTTPException

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1 

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length = 3, max_length= 512, description = 'Name of the todo')
    todo_description: str = Field(..., descritpion='Description of the todo')
    priority: Priority = Field(default = Priority.LOW, description='Priority of the Todo')


class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description= 'Unique Identifier of the todo')

class TodoUpdate(BaseModel):
    todo_name: Optional [str] = Field(None, min_length = 3, max_length= 512, description = 'Name of the todo')
    todo_description: Optional [str]= Field(None, descritpion='Description of the todo')
    priority: Optional [Priority] = Field(None, description='Priority of the Todo')



# Get, Post, Put, Delete
# get when you get information; post is when you create and submit something; put is when you change something; delet is self explanatory

#now we have to define what type of endpoint we want to define


all_todos = [
    Todo(todo_id=1 todo_name = 'sports', todo_description = "Cleaning the house", priority= Priority, HIGH)
    Todo(todo_id=2 todo_name = 'study', todo_description = "Revise Reinforcement Learning", priority= Priority, MEDIUM)
    Todo(todo_id=3 todo_name = 'meditate', todo_description = "15 minutes of meditation", priority= Priority, MEDIUM)
    Todo(todo_id=4 todo_name = 'workout', todo_description = "Plyometric workout", priority= Priority, LOW)
    Todo(todo_id=5 todo_name = 'journal', todo_description = "Write at least one page down", priority= Priority, LOW)
]


@api.get('/todos/{todo_id}',response_model = Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    
    raise HTTPException(status_code=404, detail = 'Todo not found')


@api.get('/todos', response_model = List[Todo])
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
    raise HTTPException(status_code=404, detail = 'Todo not found')


 #typecasting is the process of converting one datatype to another

@api.post('/todos', response_model= Todo)
def create_todos(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1

    new_todo = Todo(todo_id = new_todo,
                     todo_name= todo.todo_name,
                     todo_description= todo.todo_description,
                     priority = todo.priority
                     )
    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }

    all_todos.append(new_todo)

    return new_todo

    # you can use pydantic to get the proper scheme
    #you also have swagger ui to be able to view the documentation and everything (you do not necessarily need to use postman to test the endpoints themselves)

@api.put('/todos/{todo_id}', response_model = Todo)
def updated_todo(todo_id:int, updated_todo: TodoUpdate):
        for todo in all_todos:
            if todo.todo_id == todo_id:
                if updated_todo.todo_name is not None:
                    todo.todo_name = updated_todo.todo_name
                if updated_todo.todo_name is not None:
                    todo.todo_description = updated_todo.todo_description
                
                if updated_todo.todo_name is not None:
                    todo.priority = updated_todo.priority
              
                return todo
        raise HTTPException(status_code=404, detail = 'Todo not found')



@api.delete('/todos/{todo_id}', response_model = Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail = 'Todo not found')

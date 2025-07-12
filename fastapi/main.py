from typing import List, Optional
from pydantic import BaseModel, Field
from enum import IntEnum
from fastapi import FastAPI

api = FastAPI()



class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1 

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length = 3, max_length= 512)

# Get, Post, Put, Delete
# get when you get information; post is when you create and submit something; put is when you change something; delet is self explanatory

#now we have to define what type of endpoint we want to define


all_todos = [
    {'todo_id': 1 'todo_name': 'sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2 'todo_name': 'study', 'todo_description': 'revise reinforcement learning'},
    {'todo_id': 3 'todo_name': 'mediate', 'todo_description': 'mediate for 15 minutes'},
    {'todo_id': 4 'todo_name': 'code', 'todo_description': 'build a simple side project'},
    {'todo_id': 5 'todo_name': 'walk', 'todo_description': 'get 15k steps by the end of the day'},
]


@api.get('/')
def index():
    return {"message": "Hello World!"}

@api.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in all_todos:
        if todod['todo_id'] == todo_id:
            return {'result': todo}


@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

 #typecasting is the process of converting one datatype to another

@api.post('/todos')
def create_todos(todo: dict):
    new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1

    new_todo = {
        'todo_id': new_todo_id,
        'todo_name': todo['todo_name'],
        'todo_description': todo['todo_description']
    }

    all_todos.append(new_todo)

    return new_todo

    # you can use pydantic to get the proper scheme
    #you also have swagger ui to be able to view the documentation and everything (you do not necessarily need to use postman to test the endpoints themselves)

@api.put('/todos/{todo_id}')
def updated_todo(todo_id:int, updated_todo: dict):
        for todo in all_todos:
            if todo['todo_id'] == todo_id:
                todo['todo_name'] = updated_todo['todo_name']
                todo['todo_description'] = updated_todo['todo_description']
                return todo
        return "Error not found"
    

@api.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo['todo_id'] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    return "Error not found"
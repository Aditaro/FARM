from typing import List, Optional
from pydantic import BaseModel, Field
from enum import IntEnum
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Priority Enum
class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

# Base schema for all todos
class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description='Name of the todo')
    todo_description: str = Field(..., description='Description of the todo')
    priority: Priority = Field(default=Priority.LOW, description='Priority of the Todo')

# For POST endpoint
class TodoCreate(TodoBase):
    pass

# Full schema with ID
class Todo(TodoBase):
    todo_id: int = Field(..., description='Unique Identifier of the todo')

# For PATCH/PUT endpoint
class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description='Name of the todo')
    todo_description: Optional[str] = Field(None, description='Description of the todo')
    priority: Optional[Priority] = Field(None, description='Priority of the Todo')

# In-memory todo list
all_todos: List[Todo] = [
    Todo(todo_id=1, todo_name='sports', todo_description="Play football", priority=Priority.HIGH),
    Todo(todo_id=2, todo_name='study', todo_description="Revise Reinforcement Learning", priority=Priority.MEDIUM),
    Todo(todo_id=3, todo_name='meditate', todo_description="15 minutes of meditation", priority=Priority.MEDIUM),
    Todo(todo_id=4, todo_name='workout', todo_description="Plyometric workout", priority=Priority.LOW),
    Todo(todo_id=5, todo_name='journal', todo_description="Write at least one page down", priority=Priority.LOW),
]

# Retrieve one todo by ID
@app.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')

# Retrieve all todos (or first n)
@app.get('/todos', response_model=List[Todo])
def get_todos(first_n: Optional[int] = None):
    return all_todos[:first_n] if first_n else all_todos

# Create a new todo
@app.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max((t.todo_id for t in all_todos), default=0) + 1
    new_todo = Todo(
        todo_id=new_todo_id,
        todo_name=todo.todo_name,
        todo_description=todo.todo_description,
        priority=todo.priority
    )
    all_todos.append(new_todo)
    return new_todo

# Update a todo
@app.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')

# Delete a todo
@app.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            return all_todos.pop(index)
    raise HTTPException(status_code=404, detail='Todo not found')

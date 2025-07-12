# FARM Stack Learning Repository

This repository is a hands-on project for learning the FARM stack (FastAPI, React, and MongoDB). It starts with a simple FastAPI backend and will be expanded to include a frontend and a database connection.

## Current Status

The project currently consists of a FastAPI backend with an in-memory list of todos. It provides the following API endpoints:

*   `GET /todos`: Retrieve all todos.
*   `GET /todos/{todo_id}`: Retrieve a single todo by its ID.
*   `POST /todos`: Create a new todo.
*   `PUT /todos/{todo_id}`: Update an existing todo.
*   `DELETE /todos/{todo_id}`: Delete a todo.

## Setup and Running

1.  **Install dependencies:**

    ```bash
    pip install "fastapi[all]"
    ```

2.  **Run the application:**

    ```bash
    uvicorn fastapi.main:app --reload
    ```

    The application will be available at `http://127.0.0.1:8000`. You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Learning Suggestions

This repository is designed to be a learning tool. Here are some suggestions on how you can use it to learn the FARM stack:

1.  **Connect to a MongoDB database:**
    *   Replace the in-memory `all_todos` list with a MongoDB collection.
    *   You will need to use a library like `motor` to interact with MongoDB asynchronously.
    *   This will teach you how to handle database connections and perform CRUD operations in a real-world application.

2.  **Build a React frontend:**
    *   Create a new `frontend` directory and set up a React application.
    *   Use `axios` or the `fetch` API to make requests to your FastAPI backend.
    *   This will teach you how to build a user interface that interacts with a REST API.

3.  **Deploy the application:**
    *   Deploy your application to a cloud provider like Heroku, AWS, or Google Cloud.
    *   You will need to learn how to configure your application for a production environment.
    *   This will give you experience with the full software development lifecycle.

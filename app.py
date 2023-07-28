import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items, todos

app = Flask(__name__)


# stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/test")
def get_index():
    return {"message": "testing going on..."}


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.post("/todo")
def create_todo():
    todo_data = request.get_json()

    if "store_id" not in todo_data or "task" not in todo_data:
        abort(400, message="Missing required fields")

    for todo in todos.values():
        if (
            todo["store_id"] == todo_data["store_id"]
            and todo["task"] == todo_data["task"]
        ):
            abort(400, message="Item already exists")

    todo_id = uuid.uuid4().hex
    new_todo = {**todo_data, "id": todo_id}
    todos[todo_id] = new_todo
    return new_todo, 201


@app.get("/todo")
def get_all_todos():
    return {"todos": list(todos.values())}


@app.get("/todo/<string:todo_id>")
def get_todo_by_id(todo_id):
    try:
        return todos[todo_id]
    except KeyError:
        abort(404, message="Todo not found")


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")

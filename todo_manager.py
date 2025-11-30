import json
import os
from typing import List, Dict

DATA_PATH = os.path.join(os.path.dirname(__file__), "todos.json")

def ensure_data_file():
    folder = os.path.dirname(DATA_PATH)
    os.makedirs(folder, exist_ok=True)
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f, indent=2)

def load_todos() -> List[Dict]:
    ensure_data_file()
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_todos(todos: List[Dict]):
    with open(DATA_PATH, "w") as f:
        json.dump(todos, f, indent=2)

def add_todo(title: str, description: str = ""):
    todos = load_todos()
    next_id = max((t["id"] for t in todos), default=0) + 1
    todo = {"id": next_id, "title": title, "description": description, "done": False}
    todos.append(todo)
    save_todos(todos)
    return todo

def list_todos(show_all=True):
    todos = load_todos()
    if show_all:
        return todos
    return [t for t in todos if not t["done"]]

def mark_done(todo_id: int) -> bool:
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            save_todos(todos)
            return True
    return False

def delete_todo(todo_id: int) -> bool:
    todos = load_todos()
    new = [t for t in todos if t["id"] != todo_id]
    if len(new) == len(todos):
        return False
    save_todos(new)
    return True

import json
import os

TODO_FILE = os.path.join(os.path.dirname(__file__), "data", "todo_list.json")

def load_todos():
    if not os.path.exists(TODO_FILE): return []
    with open(TODO_FILE, "r", encoding="utf-8") as f: return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f: json.dump(todos, f, indent=4, ensure_ascii=False)
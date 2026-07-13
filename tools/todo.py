import json
from todo_manager import load_todos, save_todos

def register_todo_tools(mcp):
    @mcp.tool()
    async def add_todo(task: str, assignee: str) -> str:
        todos = load_todos()
        todos.append({"task": task, "assignee": assignee, "completed": False})
        save_todos(todos)
        return f"'{task}' 추가됨."

    @mcp.tool()
    async def list_todos(assignee: str = None, status: str = None) -> str:
        """할 일을 조회합니다. assignee(담당자)나 status('completed'/'pending')로 필터링 가능."""
        todos = load_todos()
        if assignee:
            todos = [t for t in todos if t["assignee"] == assignee]
        if status == "completed":
            todos = [t for t in todos if t.get("completed") == True]
        elif status == "pending":
            todos = [t for t in todos if t.get("completed") == False]
        
        return json.dumps(todos, ensure_ascii=False, indent=2) if todos else "조건에 맞는 할 일이 없습니다."
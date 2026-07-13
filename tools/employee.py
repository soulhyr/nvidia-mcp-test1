import os

def register_employee_tools(mcp):
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees")
    os.makedirs(DATA_DIR, exist_ok=True)

    @mcp.tool()
    async def save_employee_info(name: str, content: str) -> str:
        with open(os.path.join(DATA_DIR, f"{name}.md"), "w", encoding="utf-8") as f: f.write(content)
        return f"{name} 정보 저장 완료."

    @mcp.tool()
    async def search_employee_info(name: str) -> str:
        path = os.path.join(DATA_DIR, f"{name}.md")
        return open(path, "r", encoding="utf-8").read() if os.path.exists(path) else "정보 없음."
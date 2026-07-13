from mcp.server.fastmcp import FastMCP
from tools.employee import register_employee_tools
from tools.todo import register_todo_tools

mcp = FastMCP("Employee-Server")

# 도구 등록
register_employee_tools(mcp)
register_todo_tools(mcp)

if __name__ == "__main__":
    mcp.run()
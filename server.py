from mcp.server.fastmcp import FastMCP
from tools.employee import register_employee_tools
from tools.todo import register_todo_tools
from resources.policy import register_policy_resources
from prompts.prompts import register_prompts
from tools.systems import register_system_tools

mcp = FastMCP("Employee-Server")

# 도구 등록
register_employee_tools(mcp)
register_todo_tools(mcp)
register_policy_resources(mcp)
register_prompts(mcp)
register_system_tools(mcp)

if __name__ == "__main__":
    mcp.run()
from fastmcp import FastMCP
# from tools.employee import register_employee_tools
from tools.todo import register_todo_tools
# from resources.policy import register_policy_resources
# from prompts.prompts import register_prompts
# from tools.systems import register_system_tools
from tools.weather import search_weather_tools
from tools.alarm import search_alarm_tools

mcp = FastMCP("google-jam-server")

# 도구 등록
# register_employee_tools(mcp)
register_todo_tools(mcp)
# register_policy_resources(mcp)
# register_prompts(mcp)
# register_system_tools(mcp)
search_weather_tools(mcp)
search_alarm_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8001)